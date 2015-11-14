
QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets


TARGET = test
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += testmain.cpp\
        gamewindow.cpp

HEADERS  += gamewindow.h

FORMS    += gamewindow.ui
