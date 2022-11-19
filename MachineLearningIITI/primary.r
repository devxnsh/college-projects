#How we can create plots and graph. 
#we use them for extracting information from a data.

plot(1,3)


plot(c(1,3),c(5,3))

a<-c(8,4,5,7,5,3)
b<-c(8,1,4,6,8,6)
plot(a,b)

plot(1:10)

#create a line
plot(1:10,type='l')

#create a plot with title name axis nane and all

plot(1:10,main='Testing purpose',xlab='Time',ylab='Distane')

plot(1:10, col='red')

#I want to change the size of points
plot(1:10,cex=3)

#change the shape in place of circle takes something else

plot(1:10,pch=4,cex=2)  #we can use pch from 0 to 25

#Line Grpah
plot(1:10,type='l')

#change width of a line
plot(1:10,type='l',lwd=3)

#change style of a line
plot(1:10,type='l',lwd=3,lty=3) #lty can be from 0 to 6.

#create multiple lines
a=c(1,2,3,4,5,6,7,8,9)
b=c(7,2,4,1,6,8,9,4,3)
plot(a,type='l',col='red')
lines(b,type='l',col='green')
#now we can easily compare two quantity and values.


#Scatter plots
x<-c(4,2,5,6,2,8,9)
y<-c(9,0,8,3,1,0,2)
plot(x,y)

#Labelling and putting headers on scatter plot
plot(x,y,main='Testing purpose',xlab='Time',ylab='Distane')

#I have two target and to extract information from it I want to make them plot seperately in single graph
x<-c(4,2,5,6,2,8,9)
y<-c(9,0,8,3,1,0,2)

x1<-c(6,1,23,45,6,3,2,5,9,0)
y1<-c(44,1,3,5,6,3,2,0,9,3)

plot(x,y,main='Testing purpose',xlab='Time',ylab='Distane',col="blue",cex=2)
points(x1,y1,col="red",cex=2)

#Scatter plot matrics
input <- mtcars[,c('mpg','cyl')]
print(head(input))
# Give the chart file a name.
png(file = "scatterplot_matrices.png")
# Plot the matrices between 4 variables giving 12 plots.
# One variable with 3 others and total 4 variables.
pairs(~wt+mpg+disp+cyl,data = mtcars,main =
        "Scatterplot Matrix")
dev.off()

#Bar plot:
x<-c("Pricing","Status","Profit","Sales")
y<-c(9,4,3,5)
barplot(y,names.arg = x)


#Bar graph Color change
barplot(y,names.arg = x,col="Green")


#Texture change in bar graph
barplot(y,names.arg = x,density=7)

#Width changes in bar graph
barplot(y,names.arg = x,width=y)

#We wants to create a horizontal bar graph
barplot(y,names.arg = x,horiz = TRUE)


#Pie chart
x<-c(90,80,70,10)
pie(x)

#Changing starting angle in pie chart.
pie(x,init.angle = 90)

#Giving labels and headers to pie chart
labelName<-c("Small","Very small","bigger","larger")
pie(x,labels = labelName,main="Time pass")

colors<-c("red","blue","black","green")
pie(x,labels = labelName,col = colors)

#How to use legends in pie chart.
pie(x,labels = labelName,col = colors)
legend("bottomright",labelName,fill=colors)

#3D pie charts
# Get the library.
#install.packages("plotrix")
library(plotrix)
pieval<-c(2,4,6,8)
pielabels<-
  c("We hate\n pies","We oppose\n  pies","We don't\n  care","We just love pies")
# grab the radial positions of the labels
lp<-pie3D(pieval,radius=0.9,labels=pielabels,explode=0.1,main="3D PIE OPINIONS")

# lengthen the last label and move it to the left
pielabels[4]<-"We cannot survive without our pies"
lp[4]<-4.8
# specify some new colors
pie3D(pieval,radius=0.9,labels=pielabels,explode=0.1,main="3D PIE OPINIONS",
      col=c("brown","#ddaa00","pink","#dd00dd"),labelpos=lp)


#Boxplot
input <- mtcars[,c('mpg','cyl')]
print(head(input))
# Give the chart file a name.
png(file = "D:/desktop/R programs/boxplot.png")
# Plot the chart.
boxplot(mpg ~ cyl, data = mtcars, xlab =
          "Number of Cylinders", ylab = "Miles
Per Gallon", main = "Mileage Data")
# Save the file.
dev.off()

#Histogram
# Create data for the graph.
v <- c(9,13,21,8,36,22,12,41,31,33,19)
# Give the chart file a name.
png(file = "histogram.png")
# Create the histogram.
hist(v,xlab = "Weight",col = "yellow",border = "blue")
# Save the file.
dev.off()



#File handling in R programming
#R programming have so many shortcuts to build your logic and that shortcut we can use with the help of file handling

#downloading of a file.
install.packages("package name")

#importing the packages in R programming
library(fastDummies)

#statistics: 


#Disadvantages: sometime the method use in statistics are not able to give clear information about something

#example: mean median and mode. we have multiple series with us whose somertime either mean/median/mode remain same.

#analytics tools are use in such cases.

