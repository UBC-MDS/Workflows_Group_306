# runall_milestone2.sh

# run eda report
Rscript -e "rmarkdown::render('src/EDA_milestone2.Rmd')"

#Run random forest and logistic regression on the cleaned data
python src/model.py --train_file=data/elo_historic_wrangled.csv --test_file=data/elo_2019_wrangled.csv

