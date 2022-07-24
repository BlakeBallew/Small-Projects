library(tidyverse)
library(stringr)

# read csv file 
cols <- read_csv(file = "session_counts.csv");

# augment table with an extra row representing the year + month/12
# which allows us to later plot the results in chronological order from 7/12 -> 6/13
cols$month_number <- strtoi(str_sub(cols$dim_date, -2, -1))+(strtoi(sub("/.*", "", cols$dim_date)))/12


session_count <- aggregate(sessions~dim_deviceCategory+month_number, cols, sum);
transaction_count <- aggregate(transactions~dim_deviceCategory+month_number, cols, sum);
QTY_count <- aggregate(QTY~dim_deviceCategory+month_number, cols, sum);

final_result = tibble(
  session_count[1],
  session_count[2],
  session_count[3],
  transaction_count[3],
  QTY_count[3],
);

final_result$ECR <- final_result$transactions/final_result$sessions;

ggplot(final_result, aes(x=month_number, y=ECR, color=dim_deviceCategory))+geom_point();

