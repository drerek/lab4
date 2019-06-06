import collections
import sys
from datetime import datetime
from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def reader(path_to_file):
    statistics = list()
    with open(path_to_file, 'r', encoding='utf-8') as file:
        line = file.readline()
        cnt = 1
        while line and cnt < 1614878:
            statistics.append(line)
            line = file.readline()
            cnt += 1
            res = "parsing status=" + str(format((cnt / 1614878 * 100), ".2f")) + " %"
            sys.stdout.write('\r' + res)
            sys.stdout.flush()
    return statistics


def statistic_processing(statistics):
    processed_statistics = dict()
    for cnt, incident in enumerate(statistics[1:]):
        date = incident.split(",")[1]
        if date == '':
            continue
        if 2006 < int(date.split("/")[-1]) < 2010:
            if date in processed_statistics:
                processed_statistics[date] += 1
            else:
                processed_statistics[date] = 1
        res = "processing status=" + str(format((cnt / (len(statistics)-1) * 100), ".2f")) + " %"
        sys.stdout.write('\r' + res)
        sys.stdout.flush()
    sys.stdout.flush()
    return processed_statistics


def get_list_data(dict):
    list_data = list()
    for key in dict:
        list_data.append(dict[key])
    return list_data


def autoregression(list_statistics):
    model = AR(list_statistics)
    model_fit = model.fit()
    # make prediction
    yhat = model_fit.predict(len(list_statistics), len(list_statistics)+9)
    return yhat


def sarima(list_statistics):
    # SARIMA
    model = SARIMAX(list_statistics, order=(1, 1, 1), seasonal_order=(1, 1, 1, 1))
    model_fit = model.fit(disp=False)
    # make prediction
    yhat = model_fit.predict(len(list_statistics), len(list_statistics)+9)
    return yhat


def hwes(list_statistcs):
    # HWES
    model = ExponentialSmoothing(list_statistcs)
    model_fit = model.fit()
    # make prediction
    yhat = model_fit.predict(len(list_statistcs), len(list_statistcs)+9)
    return yhat


if __name__ == '__main__':
    raw_statistics = reader("NYPD_Complaint_Data_Historic.csv")
    statistics = sorted(statistic_processing(raw_statistics).items(), key=lambda x: datetime.strptime(x[0], '%m/%d/%Y'), reverse=False)
    test_statitistics = collections.OrderedDict(statistics[len(statistics)-10:])
    main_statistics = get_list_data(collections.OrderedDict(statistics[:len(statistics)-10]))
    autoregression_result = autoregression(main_statistics)
    sarima_result = sarima(main_statistics)
    hwes_result = hwes(main_statistics)
    result_file = list()
    result_file.append("Date,Origin_data,Autoregression_predicted_data,SARIMA_predicted_data,HWES_predicted_data")
    cnt = 0
    for date in test_statitistics:
        result_file.append(""+str(date)+","+str(test_statitistics[date])+","+str(int(autoregression_result[cnt]))+","+str(int(sarima_result[cnt]))+","+str(int(hwes_result[cnt])))
        cnt += 1

    with open("file.csv", "w") as file_write:
        for line in result_file:
            file_write.write(line+"\n")


