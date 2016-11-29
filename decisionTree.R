library(ISLR)

data(Hitters)
help(Hitters)
data = Hitters

names(data)
data$Years

nrow(subset(data, Years<4.5))

data = data[!is.na(data$Salary),]
attach(data)
Salary = log(Salary)
hist(Salary)

S1 = mean(Salary[Years<4.5])
exp(S1)

exp(mean(log(subset(data, Years>4.5 & Hits<117.5)$Salary)))
exp(mean(log(subset(data, Years>4.5 & Hits>117.5)$Salary)))

# grafico:

plot(Years,Hits, pch=19, col="orange")
abline(v=4.5, lwd=3)
segments(4.5,117.5 , x1 = 30, y1 = 117.5, lwd=3)
