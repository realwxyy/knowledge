# brand
BRAND = 'brand'
BRAND_PREFIX = '/brand'
BRAND_ROUTE = '/brand'
BRAND_POST_PARAMS = ['logo', 'code', 'zh_name']
BRAND_PUT_PARAMS = ['id', 'logo', 'code', 'zh_name']
BRAND_DELETE_PARAMS = ['id']
ZH_NAME = 'zh_name'

# product
PRODUCT = 'product'
PRODUCT_PREFIX = '/product'
PRODUCT_ROUTE = '/product'
PRODUCT_POST_PARAMS = ['brand_id', 'name', 'main_img', 'standard_price', 'in_stock', 'promotional_red_line_price', 'box_gauge', 'gross_weight']
PRODUCT_PUT_PARAMS = ['id', 'brand_id', 'name', 'main_img', 'standard_price', 'in_stock', 'promotional_red_line_price', 'box_gauge', 'gross_weight']
PRODUCT_DELETE_PARAMS = ['id']

# quotation
QUOTATION = 'quotation'
QUOTATION_PREFIXX = '/quotation'
QUOTATION_ROUTE = '/quotation'
QUOTATION_POST_PARAMS = ['name', 'short_name']
QUOTATION_PUT_PARAMS = ['id', 'name', 'short_name']
QUOTATION_DELETE_PARAMS = ['id']
