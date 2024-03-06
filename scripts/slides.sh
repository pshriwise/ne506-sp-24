#! /bin/bash

jupyter nbconvert "$1" --to slides --SlidesExporter.reveal_scroll=True
