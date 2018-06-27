# -*- coding : utf8 -*-
# External library pandas needed
import pandas as pd
import os
import time

IP_GEO_PATH = "../ip2loc"
LOGS_PATH = "../without_robot"
LOGS_WITH_LOCATION = "../logs_with_location"

if not os.path.exists(LOGS_WITH_LOCATION):
    os.mkdir(LOGS_WITH_LOCATION)


def is_ip(ip):
    '''judge a str is a correct ip or not'''
    # print(ip, type(ip))
    ips = [ip_bit for ip_bit in ip.split(".")[0:3]
           if int(ip_bit) >= 0 and int(ip_bit) <= 255]
    return len(ips) == 3


def is_cik(cik):
    '''judge a str is a correct cik or not'''
    # print(cik, type(cik))
    cik = str(cik)
    if cik.find('.') is not -1:
        n = len(cik)
        if cik[n - 1] is '0' and cik[n - 2] is '.':
            cik = cik[0:n - 2]
        else:
            return False

    if float(cik) <= 0 or float(cik) >= 1e11:
        return False
    return True


def find_index(interval, i):
    beg = 0
    end = len(interval) - 1
    cur = int((beg + end) / 2)

    while i < interval[cur][0] or i > interval[cur][1]:
        # print(cur, interval[cur])
        if i < interval[cur][0]:
            end = cur - 1
        elif i > interval[cur][1]:
            beg = cur + 1
        cur = int((beg + end) / 2)

    return cur


def ip_to_loc(df, ip_table):
    '''传入日志数据和loc_table,loc_table是没有ip信息的dataframe，通过ip_to_num获得IP整数,获得ips,
        '''
    ips = [(ip_to_num(ip), ip) for ip in list(set(list(df.ip)))]  # 获得[（ip_to_num,ip)...]的list，去除了重复ip.
    print("{0} ips".format(len(ips)))
    ip_loc = dict()
    for i, ip in enumerate(ips):  # enumerate可返回一个可迭代对象为IP建立索引
        index = find_index(ip_table[0], ip[0])  # 传入参数ip_table[0],实际数据中对应symbol，为和整数ip值
        ip_loc[ip[1]] = ip_table[1][index]

    return ip_loc


def ip_to_num(ip):
    '''将ip转化为整数，首先分割出IP前三段并转化成int数据类型，使用整数换算方法返回得到IP对应的整数'''
    ips = ip.split(".")[0:3]
    # print(ip)
    # print(ips)
    return int(ips[2]) + int(ips[1]) * 256 + int(ips[0]) * 256 ** 2


def fill_loc(file_name, loc_table):
    '''读入原始的日志文件，当日志文件为空，建立dataframe,存储到LOGS_WITH_LOCATION中'''
    print(file_name)
    beg = time.time()
    df = pd.read_csv(os.path.join(LOGS_PATH, file_name))
    if len(df) == 0:
        empty_df = pd.DataFrame(columns=["ip", "date", "time", "zone", "cik", "accession", "extention", "code", "size",
                                         "idx", "norefer", "noagent", "find", "crawler", "browser", "symbol", "country",
                                         "state", "city", "latitude", "longitude", "zip_code", "time_zone"])
        empty_df.to_csv(os.path.join(LOGS_WITH_LOCATION, file_name), index=None)
        return
    '''文件非空时对df apply is_ip和 is_cik函数，axis=1表示对df的列使用函数，得到ip&cik都正确的df,'''
    df = df[df.apply(lambda x: is_ip(x["ip"]) and is_cik(x["cik"]), axis=1)]

    ip_to_country = ip_to_loc(df, loc_table)

    ip_list = list(df.ip)
    symbol_list = []
    country_list = []
    state_list = []
    city_list = []
    latitude_list = []
    longitude_list = []
    zip_code_list = []
    time_zone_list = []
    n = len(df)
    for i in range(n):
        # if i % 1000 == 0:
        # print(i, "of", n)
        location = ip_to_country[ip_list[i]]
        symbol_list.append(location[0])
        country_list.append(location[1])
        state_list.append(location[2])
        city_list.append(location[3])
        latitude_list.append(location[4])
        longitude_list.append(location[5])
        zip_code_list.append(location[6])
        time_zone_list.append(location[7])

    df["symbol"] = pd.Series(symbol_list, index=df.index)
    df["country"] = pd.Series(country_list, index=df.index)
    df["state"] = pd.Series(state_list, index=df.index)
    df["city"] = pd.Series(city_list, index=df.index)
    df["latitude"] = pd.Series(latitude_list, index=df.index)
    df["longitude"] = pd.Series(longitude_list, index=df.index)
    df["zip_code"] = pd.Series(zip_code_list, index=df.index)
    df["time_zone"] = pd.Series(time_zone_list, index=df.index)
    df.to_csv(os.path.join(LOGS_WITH_LOCATION, file_name), index=None)
    print("takes {0}s".format(time.time() - beg))


def ip_to_loc_table():
    df = pd.read_csv(os.path.join(IP_GEO_PATH, "IP2LOCATION-LITE-DB11.CSV"), header=None)
    df.columns = ["start", "end", "symbol", "country", "state", "city", "latitude", "longitude", "zipcode",
                  "time_zone"]  # 原始文件没有列名，加上columns的名称。
    '''提取df中每一列为list，对start_ip&end_ip使用zip函数，再获得对应list,为index_table;
         同理获得loc_table,两个table作为最后的返回值'''
    start_list = [int(i / 256) for i in list(df.start)]  # 将整数ip转化为ip
    end_list = [int(i / 256) for i in list(df.end)]
    symbol_list = list(df.symbol)
    country_list = list(df.country)
    state_list = list(df.state)
    city_list = list(df.city)
    latitude_list = df.latitude
    longitude_list = df.longitude
    zip_code_list = df.zipcode
    time_zone_list = df.time_zone

    index_table = list(zip(start_list, end_list))
    loc_table = list(zip(symbol_list, country_list, state_list, city_list,
                         latitude_list, longitude_list, zip_code_list, time_zone_list))

    return (index_table, loc_table)


if __name__ == "__main__":
    # df = pd.read_csv(os.path.join(LOGS_PATH, "log20140101.csv"))
    loc_table = ip_to_loc_table()

    files = os.listdir(LOGS_PATH)  # 获得files文件list
    n = len(files)
    for i, file_name in enumerate(files):
        if i % 1000 == 0:
            print(i, "of", n, file_name)
        fill_loc(file_name, loc_table)
