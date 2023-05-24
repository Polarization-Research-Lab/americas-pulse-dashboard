library(tidyverse)
library(dplyr)
library(lubridate)
library(stringr)
library(data.table)
library(brms)
library(mapdata)
library(maps)
library(tidycensus)
library(rstan)
library(multidplyr)
library(tidybayes)
library(ggplot2)
library(viridis)
library(aws.s3)

#### external files

source("mrp.R")
source("recode.r")
source("mrp_functions.R")

## options

options(warn=0)
start_date <- as.Date("2022-09-16")
questions <- read.csv("assets/questions.csv", stringsAsFactors=FALSE)


full <- read.csv('../.tmp/all.csv')
full$week_ <- full$week

week_meta <-full %>% select(week,year) %>% distinct(week, .keep_all = TRUE) %>% collect()

week_meta <- as.data.frame(week_meta)

week_meta$week_labels <- paste0("w", week_meta$week, "_", week_meta$year)

#generate week labels 
week_meta$week <- lapply(week_meta$week, function (x) if (nchar(x) == 1) {return(paste0('0',x))} else {return(x)}) # <-- add leading zeros to single digit week numbers, otherwise this whole ordering scheme breaks

week_meta$sort <- paste0(week_meta$year, week_meta$week)
week_meta<-week_meta[order(week_meta$sort),]

for(i in 1: nrow(week_meta)){
  end_date <- start_date + 6
  start_month <- month.abb[month(start_date)]
  end_month <- month.abb[month(end_date)]
  if(start_month == end_month){
    week_meta$weeks[i] <- paste0(start_month, ". ", day(start_date), "-" , day(end_date))
  }else{
    week_meta$weeks[i] <- paste0(start_month, ". ", day(start_date), "-", end_month, ". ", day(end_date))
  }
  start_date <- start_date + 7
  
}


full <- recoder(full)

for(i in 1: nrow(week_meta)){
  full$week[full$week == week_meta$week[i]] <- week_meta$weeks[i]
}

week_meta$caption <- paste("Data collected",week_meta$weeks,"\nPolarizationResearchLab.com")
full$date <- as.Date(paste(full$year, full$week_, 1, sep="-"), "%Y-%U-%u")




######
# Make toplines
######
rmarkdown::render(
  'assets/topline.Rmd',
  output_file = paste0("toplines/",week_meta$week_labels[week_meta$sort == max(week_meta$sort)],'topline.pdf'), 
                  params = list(week = week_meta$weeks[week_meta$sort == max(week_meta$sort)], 
                                label = week_meta$week_labels[week_meta$sort == max(week_meta$sort)], 
                                week_number = week_meta$week[week_meta$sort == max(week_meta$sort)],  
                                year_number = week_meta$year[week_meta$sort == max(week_meta$sort)], 
                                t = "", full=""))
  
file <- paste0("toplines/", week_meta$week_labels[week_meta$sort == max(week_meta$sort)],"topline.pdf")
put_object(file, bucket="prlsurveydata")

rmarkdown::render('assets/topline.Rmd',output_file = paste0("toplines/",week_meta$week_labels[week_meta$sort == max(week_meta$sort)],'topline_engaged.pdf'), 
                  params = list(week = week_meta$weeks[week_meta$sort == max(week_meta$sort)], 
                                label = week_meta$week_labels[week_meta$sort == max(week_meta$sort)], 
                                week_number = week_meta$week[week_meta$sort == max(week_meta$sort)],  
                                year_number = week_meta$year[week_meta$sort == max(week_meta$sort)], 
                                t = "engaged", full=""))

file <- paste0("toplines/", week_meta$week_labels[week_meta$sort == max(week_meta$sort)],"topline_engaged.pdf")
put_object(file, bucket="prlsurveydata")

system("aws cloudfront create-invalidation     --distribution-id E2AKD9AJIK78QP     --paths '/*'")


rmarkdown::render('assets/topline.Rmd',output_file = paste0("toplines/all_topline_engaged.pdf"), 
                  params = list(week = week_meta$weeks[week_meta$sort == max(week_meta$sort)], 
                                label = week_meta$week_labels[week_meta$sort == max(week_meta$sort)], 
                                week_number = week_meta$week[week_meta$sort == max(week_meta$sort)],  
                                year_number = week_meta$year[week_meta$sort == max(week_meta$sort)], 
                                t = "engaged", full="full"))

file <- paste0("toplines/", week_meta$week_labels[week_meta$sort == max(week_meta$sort)],"topline_engaged.pdf")
put_object(file, bucket="prlsurveydata")


######
# Make mrp
######
run_MRP(full,questions)
