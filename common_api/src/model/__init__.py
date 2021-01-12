# dto
from src.model.dto.user import User, UserSchema
from src.model.dto.app_config import APP_CONFIG, APP_CONFIG_SCHEMA
from src.model.dto.role import Role, RoleSchema
from src.model.dto.tag import Tag, TagSchema
from src.model.dto.brand import Brand, BrandSchema
from src.model.dto.product import Product, ProductSchema
from src.model.dto.quotation import Quotation, QuotationSchema
from src.model.dto.quotation_product import QuotationProduct, QuotationProductSchema
from src.model.dto.wechat_user import WechatUser, WechatUserSchema
from src.model.dto.quotation_tag import QuotationTag, QuotationTagSchema

# popo
from src.model.popo.code2session import Code2Session
from src.model.popo.third_session import Third_Session
from src.model.popo.quotation_products import QuotationProducts, QuotationProductsSchema