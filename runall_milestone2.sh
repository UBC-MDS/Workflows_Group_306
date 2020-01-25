# runall_milestone2.sh

# download the two csv files, training set (historic) and testing set (2019)
python src/download_data.py --url="https://projects.fivethirtyeight.com/nfl-api/nfl_elo.csv" --out_file="data/elo_historic_raw.csv"
python src/download_data.py --url="https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv" --out_file="data/elo_2019_raw.csv"

# run data wrangling for both files
python src/wrangle.py --input="data/elo_historic_raw.csv" --out_dir="data/elo_historic_wrangled.csv"
python src/wrangle.py --url="data/elo_2019_raw.csv" --out_dir="data/elo_2019_wrangled.csv"

# run eda report
Rscript -e "rmarkdown::render('src/EDA_milestone2.Rmd')"

#Run random forest and logistic regression on the cleaned data
python src/model.py --train_file=data/elo_historic_wrangled.csv --test_file=data/elo_2019_wrangled.csv
