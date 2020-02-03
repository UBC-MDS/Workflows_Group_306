# runall_milestone2.sh

# download the two csv files, training set (historic) and testing set (2019)
all : Elo_prediction_report.md

data/elo_historic_raw.csv : src/download_data.py
	python src/download_data.py --url="https://projects.fivethirtyeight.com/nfl-api/nfl_elo.csv" --out_file="data/elo_historic_raw.csv"

data/elo_2019_raw.csv : src/download_data.py
	python src/download_data.py --url="https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv" --out_file="data/elo_2019_raw.csv"

# run data wrangling for both files
data/elo_historic_wrangled.csv : data/elo_historic_raw.csv src/wrangle.py
	python src/wrangle.py --input="data/elo_historic_raw.csv" --out_dir="data/elo_historic_wrangled.csv"

data/elo_2019_wrangled.csv : data/elo_2019_raw.csv src/wrangle.py
	python src/wrangle.py --input="data/elo_2019_raw.csv" --out_dir="data/elo_2019_wrangled.csv"

# run eda report
img/eda-correlation_map.png data/eda-elo_vs_result.csv img/eda-elo_lnrg.png img/eda-ELO_update_with_result.png : src/EDA_milestone3.Rmd data/elo_historic_raw.csv
	Rscript -e "rmarkdown::render('src/EDA_milestone3.Rmd', output_dir = 'doc/EDA', params = list(source = '../data/elo_historic_raw.csv', correlation = '../img/eda-correlation_map.png', elo_vs_result = '../data/eda-elo_vs_result.csv', elo_lnrg = '../img/eda-elo_lnrg.png', elo_update = '../img/eda-ELO_update_with_result.png'))"

#Run random forest and logistic regression on the cleaned data
data/lr_score.csv data/rf_score.csv img/disp_rf.jpg img/disp_lr.jpg : src/model.py data/elo_historic_wrangled.csv data/elo_2019_wrangled.csv
	python src/model.py --train_file=data/elo_historic_wrangled.csv --test_file=data/elo_2019_wrangled.csv

Elo_prediction_report.md : src/Elo_prediction_report.Rmd data/lr_score.csv data/rf_score.csv img/disp_rf.jpg img/disp_lr.jpg img/eda-ELO_update_with_result.png
	Rscript -e "rmarkdown::render('src/Elo_prediction_report.Rmd', output_dir = 'doc')"

clean :
	rm -f data/*.csv
	rm -f img/eda-*.png
	rm -f img/disp*.png
	rm -rf doc/EDA/
	rm -f doc/Elo_prediction*
