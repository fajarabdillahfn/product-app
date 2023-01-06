from . import db

'''
The "Products" resource should have the following properties:
id: any type of unique id
name: name of the product
description: description of the product
images: an list of associated images
logo_id: the primary logo for this images
created_at: timestamp
updated_at: timestamp

The "Variants" resource should have the following properties:
id: any type of unique id
product_id: id of the relevant product
name: name of the variant
size: size of the variant
color: color of the variant
images: an list of associated images
created_at: timestamp
updated_at: timestamp

The "Image" resource can have the following properties:
id: any type of unique id
url: the url of the image
'''


###Models####
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))
    variants = db.relationship('Variant', backref='product', lazy=True)
    images = db.relationship('ProductImage', backref='product', lazy=True)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    def __repr__(self):
        return 'Product {}: {}'.format(self.id, self.name)


class Variant(db.Model):
    __tablename__ = "variants"
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    name = db.Column(db.String(20))
    size = db.Column(db.String(20))
    color = db.Column(db.String(20))
    images = db.relationship('VariantImage', backref='variant', lazy=True)
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    def __repr__(self):
        return 'Variant {}:{} of Product ID {}'.format(self.id, self.name, self.productId)


class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return 'Image {}:{}'.format(self.id, self.url)


class ProductImage(db.Model):
    __tablename__ = "products_images"
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    imageID = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=False)
    isLogo = db.Column(db.Boolean)

    def __repr__(self):
        return 'Image {} of Product {}'.format(self.productId, self.imageID)


class VariantImage(db.Model):
    __tablename__ = "variants_images"
    id = db.Column(db.Integer, primary_key=True)
    variantId = db.Column(db.Integer, db.ForeignKey('variants.id'), nullable=False)
    imageID = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=False)

    def __repr__(self):
        return 'Image {} of Variant {}'.format(self.productId, self.variantId)