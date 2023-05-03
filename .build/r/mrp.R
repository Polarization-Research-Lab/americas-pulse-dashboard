rstan_options(auto_write = TRUE)

options(mc.cores = parallel::detectCores())

run_MRP <- function(df, questions){
  df <- full
  ## Put in DVs you're interested in here
  focalvar <- c(unique(questions$label))
  
  ## this will grab all data + focalvars
  df <- long_survey_data(df, focalvar)
  
  ## this recodes the demographics 
  df <- recode_pulse_dems(df)
  ## add state level vars
  df$region <- state.region[match((tigris::fips_codes$state[match(df$inputstate, as.numeric(tigris::fips_codes$state_code))]),state.abb)]

  load("assets/bidenvotes.RData")

  df$bidenvote <- x$biden_vote[match(df$inputstate,x$state_fips)]
  df$bidenvote5050 <- abs(df$bidenvote-.50)
  ## Recode Focal Variables
  df <- df %>% mutate(
    pid2 = case_when(
      pid7 < 4 ~ 'Democrat',
      pid7 > 4 ~ 'Republican'),
      infeels = case_when(
        pid2 == "Republican" ~ republican_therm_1,
        pid2 == "Democrat" ~ democrat_therm_1
      ),
      outfeels = case_when(
        pid2 == "Republican" ~ democrat_therm_1,
        pid2 == "Democrat" ~ republican_therm_1
      ),
      affpol = infeels - outfeels
    ) %>% mutate_at(vars(violence1:violence6),replace_na,0.) %>%
  mutate(general_trust=case_when(general_trust==1~1,
                                 general_trust==2~0),
         vote_importance=6-vote_importance,
         pride=6-pride,
         fair_treatment=6-fair_treatment
         )

  DVs <- c("affpol", "normindex")

  data("fips_codes")
  fips_codes$state_code <- as.numeric(fips_codes$state_code)

  for(i in 1:length(DVs)){
      print(i)
      ## Run MRP 
      bayes.mod1 <- vanilla_mrp(df, focalvar = DVs[i])

      ## Post Stratify
      post_strat_mod <- post_stratify(bayes.mod1)

      post_strat_mod$state <- tolower(fips_codes$state_name[match(post_strat_mod$STATEFIP,fips_codes$state_code)])
      post_strat_mod %>% arrange(-outcome)
      us_states <- map_data("state")
      
      m <- us_states %>% 
        left_join(post_strat_mod, by=c("region"="state"))

      write.csv(
        m[, c('region', 'outcome')], 
        file = paste0('../.tmp/', DVs[i], '-mrp.csv')
      )

      rm(bayes.mod1,post_strat)
      gc()

  }










}


