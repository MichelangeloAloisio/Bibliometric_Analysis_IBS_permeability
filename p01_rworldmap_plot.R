library(classInt)
library(RColorBrewer)
library(rworldmap)




#getting smallexample data and joining to a map
data("countryExData",envir=environment(),package="rworldmap")


country_data <- read.csv("D:/Desktop/progetti_v1/23_bibliometrics/01_file_management/Country_Production_bibliometrix_.csv", sep=';', header=TRUE)
spdf <- joinCountryData2Map(country_data, joinCode="NAME", nameJoinColumn="Country", mapResolution='coarse', verbose=TRUE)


classInt <- classIntervals( spdf[["Freq"]], n=7, style="equal")
class(classInt)


#getting a colour scheme from the RColorBrewer package
colourPalette <- RColorBrewer::brewer.pal(6,'Accent')
catMethod = classInt[["brks"]]


mapParams <- mapCountryData( spdf, nameColumnToPlot="Freq", addLegend=FALSE, catMethod = catMethod, colourPalette = colourPalette )
do.call( addMapLegend, c( mapParams, legendLabels="all", legendWidth=0.5, legendIntervals="data", legendMar = 8 ) )
do.call(addMapLegend
        ,c(mapParams
           ,legendLabels="all"
           ,legendWidth=0.5
           ,legendIntervals="data"
           ,legendMar = 2))
