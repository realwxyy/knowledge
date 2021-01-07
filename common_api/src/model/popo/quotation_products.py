from marshmallow import Schema, fields
from src.model import QuotationProductSchema


class QuotationProducts(object):
    products: list


class QuotationProductsSchema(Schema):
    class Meta:
      model = QuotationProducts
    products = fields.Nested(QuotationProductSchema, many=True)
