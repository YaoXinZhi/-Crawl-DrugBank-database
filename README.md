This program is used to crawl DrugBank database of drug information.

Originally used for Deeplearn for NLP projects, so some of the drugs that might be used as features were crawled.

In total, the name, weight, categories, DrugBank ID, and Indication information of all Biotech Drugs and all Small Drug Drugs on DrugBank were crawled.

To achieve a single page crawling, page turning, file storage, progress display.

Technical route is:
import requests
import pandas
from bs4 import BeautifulSoup
import bs4

After trying the code can run the same, only attach the results of BiotechDrug drugs, because the SmallMoleculeDrug drugs have 366 pages, all of the climb down takes about half an hour.
