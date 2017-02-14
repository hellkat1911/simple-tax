# version 2.0 of my original accounting program
# hellkat_ 9feb2017

## need to implement json-based dictionary {date:net pay} object in total_income()

# Taxes 2.0
import json
from os import exit

start = 'February 9th, 2017'

def write_info(file, i, info):
    fo = open(file, i)
    fo.write(info + "\n")
    fo.close()

def running_tax_rate():
    rtr = []
    percent = open('percent.txt', 'r')
    for line in percent:
        rtr.append(float(line))
    total = sum(rtr)/len(rtr)
    print("\nYour current tax rate is {0:.2f}% as of {1}".format(total, start))
    print("*" * 8)
    percent.close()

def total_income():
    ti = []
    f = open('records.txt', 'r')
    for line in f:
        ti.append(float(line))
    print("\nSince {0}, your total income is ${1:.2f}.".format(start, sum(ti)))
    print("*" * 8)
    f.close()

def total_taxes():
    tt = []
    dollars = open('dollar.txt', 'r')
    for line in dollars:
        tt.append(float(line))
    print("\nSince {0}, you have paid ${1:.2f} in taxes.".format(start, sum(tt)))
    print("*" * 8)
    dollars.close()

def find_taxes():
    #print("Enter the date of this pay period [mm.dd.yy]")
    #date = input('> ')
    print("\nWhat was your gross income this week?")
    gross = float(input('> '))
    print("\nWhat was your net income?")
    net = float(input('> '))

    # writes net income to records.txt
    print("Recording net income...")
    write_info('records.txt', 'a', "{0:.2f}".format(net))

    #finds taxes paid
    tax_amt = gross - net
    print("\nYou paid ${0:.2f} in taxes this week,".format(tax_amt))

    #finds taxes as percent of gross
    tax_pc = 100 - ((net / gross) * 100)
    print("which is {0:.2f}% of your gross pay.".format(tax_pc))

    #writes tax as percentage to percent.txt
    print("\nSaving tax rate...")
    write_info('percent.txt', 'a', "{0:.2f}".format(tax_pc))

    #writes tax as dollar amt to dollar.txt
    print("Saving tax amount...")
    write_info('dollar.txt', 'a', "{0:.2f}".format(tax_amt))

    print("\nSee running tax rate? [y/n]")
    see = input('> ')
    if 'y' in see:
        running_tax_rate()
    else:
        pass
    print("\nSee total pay? [y/n]")
    pay = input('> ')
    if 'y' in pay:
        total_income()
    else:
        pass
    print("\nSee total taxes paid? [y/n]")
    txpd = input('> ')
    if 'y' in txpd:
        total_taxes()
    else:
        print('Ok, exiting...')
        exit()

find_taxes()
