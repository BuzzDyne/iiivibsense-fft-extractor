# Page Structure
# Company > Organization > Factory > ProdLine > Machine > Sensor
#               APP      Serang Mill    PM2    Size Press    

PAGE_HEADER = "/html/body/div[1]/div/div[3]/div/div/div/div[1]/h4"
MENU_ITEMS = "//h6/a"

MACHINE_MENU_ITEMS = "(//table)[1]/tbody/tr/td[2]/a"

SENSOR_PAGE_CHART_CONTAINER = "/html/body/div[1]/div/div[3]/div/main/div[1]/div[3]/div[1]/div"
SENSOR_PAGE_TS                  = "//div/span/span[2]"
SENSOR_PAGE_TS_ABS          = "/html/body/div[1]/div/div[3]/div/main/div[1]/div[3]/div[1]/div/div/span/span[2]"
SENSOR_PAGE_FAULTS_CONTAINER = "/html/body/div[1]/div/div[3]/div/main/div[1]/div[2]/div[2]/div/div/div"

SENSOR_PAGE_XYZ             = "/html/body/div[1]/div/div[3]/div/main/div[1]/div[2]/div[1]/div/div[1]"
SENSOR_PAGE_SENSOR_NAME     = "/html/body/div[1]/div/div[3]/div/main/div[1]/div[3]/div[1]/div/div[1]/h4"

SENSOR_PAGE_DATA_TABLE      = "/html/body/div[1]/div/div[3]/div/main/div[1]/div[4]/div[1]/div/div[2]/div/table/tbody"
SENSOR_PAGE_DATA_TABLE_ROW      = "//tr/td/a"

SENSOR_PAGE_PEAKRMS_ROW     = "/html/body/div[1]/div/div[3]/div/main/div[1]/div[2]"
SENSOR_PAGE_GRAPH_ROW       = "/html/body/div[1]/div/div[3]/div/main/div[1]/div[3]"