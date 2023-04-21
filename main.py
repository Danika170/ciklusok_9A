import pandas as pd

if __name__ == '__main__':
    diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

    print(diamonds['carat'])
    sum = 0

    for i in diamonds['carat']:
        sum += i
    print(sum)
    darabszam = diamonds['carat'].count()
    atlag = sum / darabszam
    print('átlag: ' + str(atlag))

    for gyemant in diamonds.iterrows():
        color = gyemant[1]['color']
        if color == 'H':
            print(gyemant)
