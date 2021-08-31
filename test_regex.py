import re

if __name__ == '__main__':
    r = re.compile('GK2B_GOCI2_L2_(\d{14})_LA_S(\d{2})_G\d{2}_(\w+).nc')
    a = 'GK2B_GOCI2_L2_20190523001642_LA_S08_G08_ACR.nc'
    b = 'GK2B_GOCI2_L2_20190523021642_LA_S01_G01_aaaaACRz.nc'
    c = 'GK2B_GOCI2_L2_20190523041642_LA_S12_G12_ACdaRz.nc'
    print(r.match(b).groups())
