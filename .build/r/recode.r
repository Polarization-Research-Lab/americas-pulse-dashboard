recoder <- function(d){

  ###########
  # Party
  ###########
  d$pid <- "Independent"
  d$pid[d$pid7 < 4] <- "Democrat"
  d$pid[d$pid7  > 4 & d$pid7  <8] <- "Republican"
  
  ###########
  # Therms
  ###########
  d$inparty[d$pid == "Democrat"] <- d$democrat_therm_1[d$pid == "Democrat"]
  d$inparty[d$pid == "Republican"] <- d$republican_therm_1[d$pid == "Republican"]
  
  d$outparty[d$pid == "Republican"] <- d$democrat_therm_1[d$pid == "Republican"]
  d$outparty[d$pid == "Democrat"] <- d$republican_therm_1[d$pid == "Democrat"]
  
  d$affpol <- d$inparty - d$outparty
  
  d$affpolre[d$affpol <=0] <- NA
  d$affpolre[d$affpol >=0 & d$affpol <48] <- "Lower Third \n1-47"
  d$affpolre[d$affpol >=48 & d$affpol <75] <- "Middle Third \n48-74"
  d$affpolre[d$affpol >=75] <- "Top Third \n 75-100"
  
  ##########
  # Violence
  ##########
  
  d$violence1re <- recode(d$violence1, '1' = 1, '2' = 1, .default =0)
  d$violence2re <- recode(d$violence2, '1' = 1, '2' = 1, .default =0)
  d$violence3re <- recode(d$violence3, '1' = 1, '2' = 1, .default =0)
  d$violence4re <- recode(d$violence4, '1' = 1, '2' = 1, .default =0)
  d$violence5re <- recode(d$violence5, '1' = 1, '2' = 1, .default =0)
  d$violence6re <- recode(d$violence6, '1' = 1, '2' = 1, .default =0)
  
  d <- d %>% mutate(violence1re = ifelse(is.na(violence1re), 0, violence1re))
  d <- d %>% mutate(violence2re = ifelse(is.na(violence2re), 0, violence2re))
  d <- d %>% mutate(violence3re = ifelse(is.na(violence3re), 0, violence3re))
  d <- d %>% mutate(violence4re = ifelse(is.na(violence4re), 0, violence4re))
  d <- d %>% mutate(violence5re = ifelse(is.na(violence5re), 0, violence5re))
  d <- d %>% mutate(violence6re = ifelse(is.na(violence6re), 0, violence6re))
  
  ##########
  # Norms
  ##########

  d$norm_judgesre <- recode(d$norm_judges, '1' = 1, '2' = 1, '3' =0, '4' =0, '5'=0, .default =0)
  d$norm_pollingre <- recode(d$norm_polling, '1' = 1, '2' = 1, '3' =0, '4' =0, '5'=0, .default =0)
  d$norm_executivere <- recode(d$norm_executive, '1' = 1, '2' = 1, '3' =0, '4' =0, '5'=0, .default =0)
  d$norm_censorshipre <- recode(d$norm_censorship, '1' = 1, '2' = 1, '3' =0, '4' =0, '5'=0, .default =0)
  d$norm_loyaltyre <- recode(d$norm_loyalty, '1' = 1, '2' = 1, '3' =0, '4' =0, '5'=0, .default =0)
  
  d$normindex <- d$norm_judgesre +d$norm_pollingre +d$norm_executivere +d$norm_censorshipre +d$norm_loyaltyre
  

  ############
  # Engagement
  ############
  d$engaged <- "Not Engaged"
  
  d$engaged[d$engagement_measure ==7 & d$year == 2022 & (d$week == 39 | d$week == 40)] <- "Engaged"
  d$engaged[d$engagement_measure ==1  & !(d$year == 2022 & (d$week == 39 | d$week == 40))] <- "Engaged"
  
  ###########
  # State
  ###########
  
  d$state <- recode(d$inputstate, '1' = "Alabama",
  "2" = "Alaska",
  "4" = "Arizona",
  "5" = "Arkansas",
  "6" = "California",
  "8" = "Colorado",
  "9" = "Connecticut",
  "10" = "Delaware",
  "11" = "District of Columbia",
  "12" = "Florida",
  "13" = "Georgia",
  "15" = "Hawaii",
  "16" = "Idaho",
  "17" = "Illinois",
  "18" = "Indiana",
  "19" = "Iowa",
  "20" = "Kansas",
  "21" = "Kentucky",
  "22" = "Louisiana",
  "23" = "Maine",
  "24" = "Maryland",
  "25" = "Massachusetts",
  "26" = "Michigan",
  "27" = "Minnesota",
  "28" = "Mississippi",
  "29" = "Missouri",
  "30" = "Montana",
  "31" = "Nebraska",
  "32" = "Nevada",
  "33" = "New Hampshire",
  "34" = "New Jersey",
  "35" = "New Mexico",
  "36" = "New York",
  "37" = "North Carolina",
  "38" = "North Dakota",
  "39" = "Ohio",
  "40" = "Oklahoma",
  "41" = "Oregon",
  "42" = "Pennsylvania",
  "44" = "Rhode Island",
  "45" = "South Carolina",
  "46" = "South Dakota",
  "47" = "Tennessee",
  "48" = "Texas",
  "49" = "Utah",
  "50" = "Vermont",
  "51" = "Virginia",
  "53" = "Washington",
  "54" = "West Virginia",
  "55" = "Wisconsin",
  "56" = "Wyoming")
  
  ###############
  # Religion
  ###############
  
  d$bornagain <- "Not born again"
  d$bornagain[d$pew_bornagain == 1] <- "Born again"
  
  
  ###############
  # Date and time
  ###############
  d$date <- as.POSIXct(strptime(d$starttime, format="%Y-%m-%dT%H:%M:%S",tz="UTC"))
  d$date <- as.Date(format(d$date, tz="America/Los_Angeles",usetz=TRUE))
  
  return(d)
}

wrapper <- function(x, width=40) 
{
  paste(strwrap(x, width), collapse = "\n")
}

weighted.ci <- function(x, weights, conf.level = 0.95) {
  require(Hmisc)
  nx <- length(x)
  df <- nx - 1
  vx <- wtd.var(x, weights, normwt = TRUE) ## From Hmisc
  mx <- weighted.mean(x, weights, na.rm=T)
  stderr <- sqrt(vx/nx)
  tstat <- mx/stderr ## not mx - mu
  alpha <- 1 - conf.level
  cint <- qt(1 - alpha/2, df)
  cint <- tstat + c(-cint, cint)
  cint * stderr
}


