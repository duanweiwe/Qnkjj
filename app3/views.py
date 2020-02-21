# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app3 import forms
from app3 import models
from p2.settings import BASE_DIR
from django.http import StreamingHttpResponse, HttpResponse

from django.template.loader import get_template
from xhtml2pdf import pisa

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from xhtml2pdf.default import DEFAULT_FONT

import shutil
import PyPDF2
import StringIO


import datetime
import os
import pypinyin
import pdfkit
import xlwt


