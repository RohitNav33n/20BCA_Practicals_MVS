getwd()
setwd("C:/Users/ROHIT/OneDrive/Desktop/RSTUDIO DATA")
data=read.csv("CarPrice_Assignment.csv")
View(data)
head(data)
mean(data$enginesize)

t.test(data$enginesize,mu=100)
