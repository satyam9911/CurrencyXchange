create database CurrencyXchange
use CurrencyXchange
create table userConfidentialData (username nvarchar(20) primary key, password nvarchar(20))
create table userTransactionsData(username nvarchar(20) primary key, transactionType varchar(2), transactionTime datetime, amount int)
create table userWalletData(username nvarchar(20) primary key, currentBalance nvarchar(20))
create table user_profile_picture (username nvarchar(20) primary key, profile_Picture varbinary(max))