library(tidyverse)
library(stringr)
library(data.table)
library(openxlsx)
options(scipen = 10)

# make workbook
workbook <- createWorkbook();

# read csv file 
cols <- read_csv(file = "session_counts.csv");

# augment table with an extra row representing the year + month/12
# which allows us to later plot the results in chronological order from 7/12 -> 6/13
cols$year_after_2000 <- strtoi(str_sub(cols$dim_date, -2, -1))+(strtoi(sub("/.*", "", cols$dim_date)))/12


session_count <- aggregate(sessions~dim_deviceCategory+year_after_2000, cols, sum);
transaction_count <- aggregate(transactions~dim_deviceCategory+year_after_2000, cols, sum);
QTY_count <- aggregate(QTY~dim_deviceCategory+year_after_2000, cols, sum);

table1_result <- tibble(
  session_count[1],
  session_count[2],
  session_count[3],
  transaction_count[3],
  QTY_count[3],
);

table1_result$ECR <- table1_result$transactions/table1_result$sessions;



carts_data <- read_csv(file = "adds_to_cart.csv");
carts_data$year_after_2000 <- (carts_data$dim_year %% 1000)+(carts_data$dim_month/12)


# populate table to be used for second xslx worksheet
table2_data <- aggregate(.~year_after_2000, table1_result[c(2,3,4,5)], sum)[c(11,12), ]  # grouping by month and selecting last 2
table2_data$ECR <- table2_data$transactions/table2_data$sessions  # adding ECR column
table2_data <- cbind(table2_data, carts_data[c(11,12),3]) # adding addsToCard column
table2_data <- table2_data[,c(2,3,4,5,6)]   # cutting out year_after_2000 row

table2_data <- as.data.frame(t(as.matrix(table2_data)))
table2_data$absolute_diff <- table2_data$"12"-table2_data$"11";
table2_data$relative_diff <- table2_data$"12"/table2_data$"11";

key <- c("sessions", "transactions", "QTY", "ECR", "addsToCart");
table2_data <- cbind(key, table2_data);

colnames(table2_data) <- c("metric", "5/13", "6/13", "absolute_diff", "relative_diff");


# produce a nice little plot that allows us to better visualize the site traffic data
# changing  transactions to sessions and ECR yields the additional plots found in the deliverable
ggplot(table1_result, aes(x=year_after_2000, y=transactions, color=dim_deviceCategory, group=dim_deviceCategory))+geom_line()+geom_point();

# last thing we need to do is add worksheets to the workbook

addWorksheet(workbook, "worksheet_no1")
addWorksheet(workbook, "worksheet_no2")

table1_result <- as.data.frame(table1_result);

writeData(workbook, "worksheet_no1", table1_result)
writeData(workbook, "worksheet_no2", table2_data)
saveWorkbook(workbook, file = "analysis_results.xlsx", overwrite = TRUE);

