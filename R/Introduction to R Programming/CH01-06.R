getwd() # get current workspace
setwd("D:/Hossein/My GitHub Web Design/DataScience/R/Introduction to Data Analytics with R") # set workspace

# some logical function in R

x <- c(1,4,5,7,9,13)
y <- c(10, 37, 53, 68, 81, 118)
x == 4 # FALSE  TRUE FALSE FALSE FALSE FALSE
which(x==4) # 2
any(x>9) # TRUE
all(x>14) # FALSE
all(x>0) # TRUE
x !=4 # TRUE FALSE  TRUE  TRUE  TRUE  TRUE
# & |
any(x>4) & any(x<13) # TRUE

