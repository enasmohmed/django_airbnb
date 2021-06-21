from modeltranslation.translator import TranslationOptions, translator

from property.models import Category, Property, Place, PropertyReview


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class PropertyTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


class PlaceTranslationOptions(TranslationOptions):
    fields = ('name',)


class PropertyReviewTranslationOptions(TranslationOptions):
    fields = ('property', 'feedback',)


translator.register(Category, CategoryTranslationOptions)
translator.register(PropertyReview, PropertyReviewTranslationOptions)
translator.register(Place, CategoryTranslationOptions)
translator.register(Property, PropertyTranslationOptions)
