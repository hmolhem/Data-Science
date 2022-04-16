# vector in R
d1 <- c(1,2,3,4,5)
d2 <- c("Ali","Babak","Sara")
d3 <- c(TRUE,FALSE)
d4 <- 1:10
d5 <- seq(1,10, by =2)
d6 <- seq(1,10, length = 4)
d7 <- rep (1, 5)
d8 <- rep (1:3, 5)

# How to access a element in R vector?
d1[1] # 1
d2[3] # "sara"
d3[1] # TRUE
d6[4] # 10
# point: first index start with 1 in R

# sort of vector
sort(d1, decreasing = TRUE) # Descending
sort(d1, decreasing = FALSE) # Ascending
