#!/bin/sh

app=./console_app.py

$app --create AC4,AD10,BE3,CD4,CF2,DE1,EB3,EA2,FD1
$app --update AB1

$app --cost ABE
$app --cost AD
$app --cost EACF
$app --cost ADF

$app --count ED --hop_limit 4
$app --count EE
$app --count EE --use_twice --cost_limit 20

$app --cheap ED
$app --cheap EE

$app --delete
