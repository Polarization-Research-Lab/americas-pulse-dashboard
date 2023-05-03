## load post-stratification data
load("assets/poststrat.RData")

post_stratify <- function(bayes.mod){
  cluster <- new_cluster(15)
  bayes.mod %>%
    add_predicted_draws(newdata=post_strat, allow_new_levels=TRUE) %>%
    rename(outcome = .prediction) %>%
    mean_qi() %>%
    mutate(outcome = outcome * state_per) %>%
    group_by(STATEFIP) %>%
    summarise(outcome = sum(outcome))
  }

## Recode Pulse for MRP
recode_pulse_dems <- function(df) {
  df<- df %>% mutate(
    age  = 2022 - as.numeric(df$birthyr),
    race6 = case_when(
      race == 1 & hispanic == 2 ~ 1,
      race == 2 & hispanic == 2 ~ 2,
      race == 4 &  hispanic == 2 ~ 4,
      race == 5 & hispanic == 2 ~ 5,
      hispanic == 1 ~ 3,
      TRUE ~ 6
    ),
    gender = case_when(gender == 1 ~ 1,
                       gender == 2 ~ 2),
    age = case_when(
      age < 25 & age >= 18 ~ 1,
      age >= 25 & age <= 34 ~ 2,
      age >= 35 & age <= 44 ~ 3,
      age >= 45 & age <= 64 ~ 4,
      age >= 65 ~ 5
    ),
    educ4 = case_when(
      educ %in% c(1, 2) ~ 1,
      educ %in% c(3, 4) ~ 2,
      educ %in% c(5) ~ 3,
      educ %in% c(6) ~ 4
    ),
    STATEFIP = inputstate,
    race_gender = interaction(race6, gender),
    age_educ = interaction(age, educ4)
  )
 return(df) 
}

vanilla_mrp <- function(df, focalvar){
  fm <-
    as.formula(paste(
      focalvar,
      "~ (1 | STATEFIP) + (1 | age) + (1 | race6) + (1|gender) + (1|educ4)+(1|age_educ)+(1|race_gender) + region + bidenvote+bidenvote5050"
      ))
  brm(
    fm,cores = parallel::detectCores(),
    data = df,
    family = gaussian(),
    prior = c(
      set_prior("normal(0,0.2)", class = 'sd', group = "gender"),
      set_prior("normal(0,0.2)", class = 'sd', group =
                  "age"),
      set_prior("normal(0,0.2)", class = 'sd', group =
                  "educ4"),
      set_prior("normal(0,0.2)", class = 'sd', group =
                  "race6"),
      set_prior("normal(0,0.2)", class = 'sd', group =
                  "STATEFIP"),
      set_prior("normal(0,0.2)", class = 'sd', group =
                  "age_educ"),
      set_prior("normal(0,0.2)", class = 'sd', group =
                  "race_gender")
    ),
    iter = 2000,
  )

}

long_survey_data <- function(df, vars){
  otherdems <- c("race","hispanic","birthyr","educ","inputstate","gender","pid7","starttime")
  df %>%     select(c(vars, otherdems))
  return(df)
}

