# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:13:22 2019

@author: marti
"""
import pandas as pd

ba = pd.read_excel("resultados_2015_nacionales_presidente_y_vicepresidente.xlsx", "Buenos Aires")

ba.columns = ["col1","col2","col3","col4" ]