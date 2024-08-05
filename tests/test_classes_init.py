def test_init_product_class(products_iphon):
    assert products_iphon.name == "Iphone 15"
    assert products_iphon.description == "512GB, Gray space"
    assert products_iphon.price == 210000.0
    assert products_iphon.quantity == 8


def test_init_category_class(class_smartphon):
    assert class_smartphon.name == "Смартфоны"
    assert (
        class_smartphon.description
        == """Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"""
    )
    assert class_smartphon.product_count == 3
    assert class_smartphon.category_count == 1
