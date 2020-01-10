def create():
    UK= open("UK.csv","x")
    UK.write("TemplateType=fptcustom;Version=2019.0519;Templatpedito dallo stesso giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Eignature=U0hJUlQ=;The top 3 rows are for Amazon.com use only. Do not modify or delete the top 3 rows.;;;;;;;;;;;;;;;Imagpedito dallo stesso giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;E;;;;;;;;Variation;;;;Basic;;;;;;;;Discovery;;;;;;;;;;;;;;;;;Product Enrichment;;;;Dimensions;;;;;;;;;Fulfillment;;;;;;;Compliance;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Offer;;;;;;;;;;;;;;;;;;;;;;;b2b;;;;;;;;;;;;;;\n")
    UK.write("Product Type;Seller SKU;Brand Name;Product ID;Product ID Type;Product Name;Recommended Browse Nodes;Outer Material Type;Material Composition;Colour Map;Colour;Size;Department;Size Map;Adult Flag;Standard Price;Quantity;Main Image Url;Other Image Url1;Other Image Url2;Other Image Url3;Other Image Url4;Other Image Url5;Other Image Url6;Other Image Url7;Other Image Url8;Parentage;Parent SKU;Relationship Type;Variation Theme;Update Delete;Product Description;Inner Material Type;Product Care Instructions;Model Name;Model Number;Manufacturer Part Number;Product Exemption Reason;Search Terms;Season and collection year;Pattern description;Occasion description;Fitting type;Key Product Features;Key Product Features;Key Product Features;Key Product Features;Key Product Features;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;Season;material_type;Style Name;Sleeve Type;Collar Style;size-modifier;Neck size;Neck Size unit;Shipping Weight;Website Shipping Weight Unit Of Measure;Item Width;Item Height;Item Shape;Item Dimensions Unit Of Measure;Item Length;Fulfillment Centre ID;Package Length;package-width;Package Height;Package Weight;Package Weight Unit Of Measure;Package Dimensions Unit Of Measure;Legal Disclaimer Description;Safety Warning;EU Toys Safety Directive Age-specific warning;EU Toys Safety Directive Non-Age-specific warning;EU Toys Safety Directive language warning;Country/Region Of Origin;Is this product a battery or does it utilise batteries?;Batteries are Included;Battery composition;Battery type/size;Battery type/size;Battery type/size;Number of batteries;Number of batteries;Number of batteries;Battery weight (grams);battery_weight_unit_of_measure;Number of Lithium Metal Cells;Number of Lithium-ion Cells;Lithium Battery Packaging;Watt hours per battery;lithium_battery_energy_content_unit_of_measure;Lithium content (grams);lithium_battery_weight_unit_of_measure;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;UN number;Safety Data Sheet (SDS) URL;Item Weight;item_weight_unit_of_measure;Volume;item_volume_unit_of_measure;Flash point (°C)?;Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Condition Type;condition_note;Currency;Handling Time;Sale Price;Sale From Date;Sale End Date;max-aggregate-ship-quantity;Package Quantity;Number of Items;Can Be Gift Messaged;Is Gift Wrap Available?;Is Discontinued by Manufacturer;Launch Date;Restock Date;Recommended Retail Price;Stop Selling Date;Max Order Quantity;Merchant Shipping Group;Offering Release Date;Scheduled Delivery SKU List;RRP;Product Tax Code;Business Price;Quantity Price Type;Quantity Lower Bound 1;Quantity Price 1;Quantity Lower Bound 2;Quantity Price 2;Quantity Lower Bound 3;Quantity Price 3;Quantity Lower Bound 4;Quantity Price 4;Quantity Lower Bound 5;Quantity Price 5;National Stock Number;United Nations Standard Products and Services Code;Pricing Action\n")
    UK.write("feed_product_type;item_sku;brand_name;external_product_id;external_product_id_type;item_name;recommended_browse_nodes;outer_material_type;material_composition;color_map;color_name;size_name;department_name;size_map;is_adult_product;standard_price;quantity;main_image_url;other_image_url1;other_image_url2;other_image_url3;other_image_url4;other_image_url5;other_image_url6;other_image_url7;other_image_url8;parent_child;parent_sku;relationship_type;variation_theme;update_delete;product_description;inner_material_type;care_instructions;model_name;model;part_number;gtin_exemption_reason;generic_keywords;collection_name;pattern_type;lifestyle;fit_type;bullet_point1;bullet_point2;bullet_point3;bullet_point4;bullet_point5;platinum_keywords1;platinum_keywords2;platinum_keywords3;platinum_keywords4;platinum_keywords5;seasons;material_type;style_name;sleeve_type;collar_style;special_size_type;neck_size;neck_size_unit_of_measure;website_shipping_weight;website_shipping_weight_unit_of_measure;item_width;item_height;item_shape;item_dimensions_unit_of_measure;item_length;fulfillment_center_id;package_length;package_width;package_height;package_weight;package_weight_unit_of_measure;package_dimensions_unit_of_measure;legal_disclaimer_description;safety_warning;eu_toys_safety_directive_age_warning;eu_toys_safety_directive_warning;eu_toys_safety_directive_language;country_of_origin;batteries_required;are_batteries_included;battery_cell_composition;battery_type1;battery_type2;battery_type3;number_of_batteries1;number_of_batteries2;number_of_batteries3;battery_weight;battery_weight_unit_of_measure;number_of_lithium_metal_cells;number_of_lithium_ion_cells;lithium_battery_packaging;lithium_battery_energy_content;lithium_battery_energy_content_unit_of_measure;lithium_battery_weight;lithium_battery_weight_unit_of_measure;supplier_declared_dg_hz_regulation1;supplier_declared_dg_hz_regulation2;supplier_declared_dg_hz_regulation3;supplier_declared_dg_hz_regulation4;supplier_declared_dg_hz_regulation5;hazmat_united_nations_regulatory_id;safety_data_sheet_url;item_weight;item_weight_unit_of_measure;item_volume;item_volume_unit_of_measure;flash_point;ghs_classification_class1;ghs_classification_class2;ghs_classification_class3;condition_type;condition_note;currency;fulfillment_latency;sale_price;sale_from_date;sale_end_date;max_aggregate_ship_quantity;item_package_quantity;number_of_items;offering_can_be_gift_messaged;offering_can_be_giftwrapped;is_discontinued_by_manufacturer;product_site_launch_date;restock_date;list_price;offering_end_date;max_order_quantity;merchant_shipping_group_name;offering_start_date;delivery_schedule_group_id;uvp_list_price;product_tax_code;business_price;quantity_price_type;quantity_lower_bound1;quantity_price1;quantity_lower_bound2;quantity_price2;quantity_lower_bound3;quantity_price3;quantity_lower_bound4;quantity_price4;quantity_lower_bound5;quantity_price5;national_stock_number;unspsc_code;pricing_action\n")
    UK.write(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    UK.write(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    DE= open("DE.csv", "x")
    DE.write(
        "TemplateType=fptcustom;Version=2019.0519;TemplateSignature=U0hJUlQ=;The top 3 rows are for Amazon.com use only. Do not modify or delete the top 3 rows.;;;;;;;;;;;;;;;Images;;;;;;;;Variation;;;;Basic;;;;;;;;Discovery;;;;;;;;;;;;;;;;;Product Enrichment;;;;Dimensions;;;;;;;;;Fulfillment;;;;;;;Compliance;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Offer;;;;;;;;;;;;;;;;;;;;;;;b2b;;;;;;;;;;;;;;”)\n")
    DE.write(
        "Product Type;Seller SKU;Brand Name;Product ID;Product ID Type;Product Name;Recommended Browse Nodes;Outer Material Type;Material Composition;Colour Map;Colour;Size;Department;Size Map;Adult Flag;Standard Price;Quantity;Main Image Url;Other Image Url1;Other Image Url2;Other Image Url3;Other Image Url4;Other Image Url5;Other Image Url6;Other Image Url7;Other Image Url8;Parentage;Parent SKU;Relationship Type;Variation Theme;Update Delete;Product Description;Inner Material Type;Product Care Instructions;Model Name;Model Number;Manufacturer Part Number;Product Exemption Reason;Search Terms;Season and collection year;Pattern description;Occasion description;Fitting type;Key Product Features;Key Product Features;Key Product Features;Key Product Features;Key Product Features;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;Season;material_type;Style Name;Sleeve Type;Collar Style;size-modifier;Neck size;Neck Size unit;Shipping Weight;Website Shipping Weight Unit Of Measure;Item Width;Item Height;Item Shape;Item Dimensions Unit Of Measure;Item Length;Fulfillment Centre ID;Package Length;package-width;Package Height;Package Weight;Package Weight Unit Of Measure;Package Dimensions Unit Of Measure;Legal Disclaimer Description;Safety Warning;EU Toys Safety Directive Age-specific warning;EU Toys Safety Directive Non-Age-specific warning;EU Toys Safety Directive language warning;Country/Region Of Origin;Is this product a battery or does it utilise batteries?;Batteries are Included;Battery composition;Battery type/size;Battery type/size;Battery type/size;Number of batteries;Number of batteries;Number of batteries;Battery weight (grams);battery_weight_unit_of_measure;Number of Lithium Metal Cells;Number of Lithium-ion Cells;Lithium Battery Packaging;Watt hours per battery;lithium_battery_energy_content_unit_of_measure;Lithium content (grams);lithium_battery_weight_unit_of_measure;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;UN number;Safety Data Sheet (SDS) URL;Item Weight;item_weight_unit_of_measure;Volume;item_volume_unit_of_measure;Flash point (°C)?;Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Condition Type;condition_note;Currency;Handling Time;Sale Price;Sale From Date;Sale End Date;max-aggregate-ship-quantity;Package Quantity;Number of Items;Can Be Gift Messaged;Is Gift Wrap Available?;Is Discontinued by Manufacturer;Launch Date;Restock Date;Recommended Retail Price;Stop Selling Date;Max Order Quantity;Merchant Shipping Group;Offering Release Date;Scheduled Delivery SKU List;RRP;Product Tax Code;Business Price;Quantity Price Type;Quantity Lower Bound 1;Quantity Price 1;Quantity Lower Bound 2;Quantity Price 2;Quantity Lower Bound 3;Quantity Price 3;Quantity Lower Bound 4;Quantity Price 4;Quantity Lower Bound 5;Quantity Price 5;National Stock Number;United Nations Standard Products and Services Code;Pricing Action\n")
    DE.write(
        "feed_product_type;item_sku;brand_name;external_product_id;external_product_id_type;item_name;recommended_browse_nodes;outer_material_type;material_composition;color_map;color_name;size_name;department_name;size_map;is_adult_product;standard_price;quantity;main_image_url;other_image_url1;other_image_url2;other_image_url3;other_image_url4;other_image_url5;other_image_url6;other_image_url7;other_image_url8;parent_child;parent_sku;relationship_type;variation_theme;update_delete;product_description;inner_material_type;care_instructions;model_name;model;part_number;gtin_exemption_reason;generic_keywords;collection_name;pattern_type;lifestyle;fit_type;bullet_point1;bullet_point2;bullet_point3;bullet_point4;bullet_point5;platinum_keywords1;platinum_keywords2;platinum_keywords3;platinum_keywords4;platinum_keywords5;seasons;material_type;style_name;sleeve_type;collar_style;special_size_type;neck_size;neck_size_unit_of_measure;website_shipping_weight;website_shipping_weight_unit_of_measure;item_width;item_height;item_shape;item_dimensions_unit_of_measure;item_length;fulfillment_center_id;package_length;package_width;package_height;package_weight;package_weight_unit_of_measure;package_dimensions_unit_of_measure;legal_disclaimer_description;safety_warning;eu_toys_safety_directive_age_warning;eu_toys_safety_directive_warning;eu_toys_safety_directive_language;country_of_origin;batteries_required;are_batteries_included;battery_cell_composition;battery_type1;battery_type2;battery_type3;number_of_batteries1;number_of_batteries2;number_of_batteries3;battery_weight;battery_weight_unit_of_measure;number_of_lithium_metal_cells;number_of_lithium_ion_cells;lithium_battery_packaging;lithium_battery_energy_content;lithium_battery_energy_content_unit_of_measure;lithium_battery_weight;lithium_battery_weight_unit_of_measure;supplier_declared_dg_hz_regulation1;supplier_declared_dg_hz_regulation2;supplier_declared_dg_hz_regulation3;supplier_declared_dg_hz_regulation4;supplier_declared_dg_hz_regulation5;hazmat_united_nations_regulatory_id;safety_data_sheet_url;item_weight;item_weight_unit_of_measure;item_volume;item_volume_unit_of_measure;flash_point;ghs_classification_class1;ghs_classification_class2;ghs_classification_class3;condition_type;condition_note;currency;fulfillment_latency;sale_price;sale_from_date;sale_end_date;max_aggregate_ship_quantity;item_package_quantity;number_of_items;offering_can_be_gift_messaged;offering_can_be_giftwrapped;is_discontinued_by_manufacturer;product_site_launch_date;restock_date;list_price;offering_end_date;max_order_quantity;merchant_shipping_group_name;offering_start_date;delivery_schedule_group_id;uvp_list_price;product_tax_code;business_price;quantity_price_type;quantity_lower_bound1;quantity_price1;quantity_lower_bound2;quantity_price2;quantity_lower_bound3;quantity_price3;quantity_lower_bound4;quantity_price4;quantity_lower_bound5;quantity_price5;national_stock_number;unspsc_code;pricing_action\n")
    DE.write(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    DE.write(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    FR= open("FR.csv", "x")
    FR.write(
        "TemplateType=fptcustom;Version=2019.0519;TemplateSignature=U0hJUlQ=;The top 3 rows are for Amazon.com use only. Do not modify or delete the top 3 rows.;;;;;;;;;;;;;;;Images;;;;;;;;Variation;;;;Basic;;;;;;;;Discovery;;;;;;;;;;;;;;;;;Product Enrichment;;;;Dimensions;;;;;;;;;Fulfillment;;;;;;;Compliance;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Offer;;;;;;;;;;;;;;;;;;;;;;;b2b;;;;;;;;;;;;;;”)\n")
    FR.write(
        "Product Type;Seller SKU;Brand Name;Product ID;Product ID Type;Product Name;Recommended Browse Nodes;Outer Material Type;Material Composition;Colour Map;Colour;Size;Department;Size Map;Adult Flag;Standard Price;Quantity;Main Image Url;Other Image Url1;Other Image Url2;Other Image Url3;Other Image Url4;Other Image Url5;Other Image Url6;Other Image Url7;Other Image Url8;Parentage;Parent SKU;Relationship Type;Variation Theme;Update Delete;Product Description;Inner Material Type;Product Care Instructions;Model Name;Model Number;Manufacturer Part Number;Product Exemption Reason;Search Terms;Season and collection year;Pattern description;Occasion description;Fitting type;Key Product Features;Key Product Features;Key Product Features;Key Product Features;Key Product Features;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;Season;material_type;Style Name;Sleeve Type;Collar Style;size-modifier;Neck size;Neck Size unit;Shipping Weight;Website Shipping Weight Unit Of Measure;Item Width;Item Height;Item Shape;Item Dimensions Unit Of Measure;Item Length;Fulfillment Centre ID;Package Length;package-width;Package Height;Package Weight;Package Weight Unit Of Measure;Package Dimensions Unit Of Measure;Legal Disclaimer Description;Safety Warning;EU Toys Safety Directive Age-specific warning;EU Toys Safety Directive Non-Age-specific warning;EU Toys Safety Directive language warning;Country/Region Of Origin;Is this product a battery or does it utilise batteries?;Batteries are Included;Battery composition;Battery type/size;Battery type/size;Battery type/size;Number of batteries;Number of batteries;Number of batteries;Battery weight (grams);battery_weight_unit_of_measure;Number of Lithium Metal Cells;Number of Lithium-ion Cells;Lithium Battery Packaging;Watt hours per battery;lithium_battery_energy_content_unit_of_measure;Lithium content (grams);lithium_battery_weight_unit_of_measure;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;UN number;Safety Data Sheet (SDS) URL;Item Weight;item_weight_unit_of_measure;Volume;item_volume_unit_of_measure;Flash point (°C)?;Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Condition Type;condition_note;Currency;Handling Time;Sale Price;Sale From Date;Sale End Date;max-aggregate-ship-quantity;Package Quantity;Number of Items;Can Be Gift Messaged;Is Gift Wrap Available?;Is Discontinued by Manufacturer;Launch Date;Restock Date;Recommended Retail Price;Stop Selling Date;Max Order Quantity;Merchant Shipping Group;Offering Release Date;Scheduled Delivery SKU List;RRP;Product Tax Code;Business Price;Quantity Price Type;Quantity Lower Bound 1;Quantity Price 1;Quantity Lower Bound 2;Quantity Price 2;Quantity Lower Bound 3;Quantity Price 3;Quantity Lower Bound 4;Quantity Price 4;Quantity Lower Bound 5;Quantity Price 5;National Stock Number;United Nations Standard Products and Services Code;Pricing Action\n")
    FR.write(
        "feed_product_type;item_sku;brand_name;external_product_id;external_product_id_type;item_name;recommended_browse_nodes;outer_material_type;material_composition;color_map;color_name;size_name;department_name;size_map;is_adult_product;standard_price;quantity;main_image_url;other_image_url1;other_image_url2;other_image_url3;other_image_url4;other_image_url5;other_image_url6;other_image_url7;other_image_url8;parent_child;parent_sku;relationship_type;variation_theme;update_delete;product_description;inner_material_type;care_instructions;model_name;model;part_number;gtin_exemption_reason;generic_keywords;collection_name;pattern_type;lifestyle;fit_type;bullet_point1;bullet_point2;bullet_point3;bullet_point4;bullet_point5;platinum_keywords1;platinum_keywords2;platinum_keywords3;platinum_keywords4;platinum_keywords5;seasons;material_type;style_name;sleeve_type;collar_style;special_size_type;neck_size;neck_size_unit_of_measure;website_shipping_weight;website_shipping_weight_unit_of_measure;item_width;item_height;item_shape;item_dimensions_unit_of_measure;item_length;fulfillment_center_id;package_length;package_width;package_height;package_weight;package_weight_unit_of_measure;package_dimensions_unit_of_measure;legal_disclaimer_description;safety_warning;eu_toys_safety_directive_age_warning;eu_toys_safety_directive_warning;eu_toys_safety_directive_language;country_of_origin;batteries_required;are_batteries_included;battery_cell_composition;battery_type1;battery_type2;battery_type3;number_of_batteries1;number_of_batteries2;number_of_batteries3;battery_weight;battery_weight_unit_of_measure;number_of_lithium_metal_cells;number_of_lithium_ion_cells;lithium_battery_packaging;lithium_battery_energy_content;lithium_battery_energy_content_unit_of_measure;lithium_battery_weight;lithium_battery_weight_unit_of_measure;supplier_declared_dg_hz_regulation1;supplier_declared_dg_hz_regulation2;supplier_declared_dg_hz_regulation3;supplier_declared_dg_hz_regulation4;supplier_declared_dg_hz_regulation5;hazmat_united_nations_regulatory_id;safety_data_sheet_url;item_weight;item_weight_unit_of_measure;item_volume;item_volume_unit_of_measure;flash_point;ghs_classification_class1;ghs_classification_class2;ghs_classification_class3;condition_type;condition_note;currency;fulfillment_latency;sale_price;sale_from_date;sale_end_date;max_aggregate_ship_quantity;item_package_quantity;number_of_items;offering_can_be_gift_messaged;offering_can_be_giftwrapped;is_discontinued_by_manufacturer;product_site_launch_date;restock_date;list_price;offering_end_date;max_order_quantity;merchant_shipping_group_name;offering_start_date;delivery_schedule_group_id;uvp_list_price;product_tax_code;business_price;quantity_price_type;quantity_lower_bound1;quantity_price1;quantity_lower_bound2;quantity_price2;quantity_lower_bound3;quantity_price3;quantity_lower_bound4;quantity_price4;quantity_lower_bound5;quantity_price5;national_stock_number;unspsc_code;pricing_action\n")
    FR.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    FR.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    IT= open("IT.csv", "x")
    IT.write(
        "TemplateType=fptcustom;Version=2019.0519;TemplateSignature=U0hJUlQ=;The top 3 rows are for Amazon.com use only. Do not modify or delete the top 3 rows.;;;;;;;;;;;;;;;Images;;;;;;;;Variation;;;;Basic;;;;;;;;Discovery;;;;;;;;;;;;;;;;;Product Enrichment;;;;Dimensions;;;;;;;;;Fulfillment;;;;;;;Compliance;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Offer;;;;;;;;;;;;;;;;;;;;;;;b2b;;;;;;;;;;;;;;”)\n")
    IT.write(
        "Product Type;Seller SKU;Brand Name;Product ID;Product ID Type;Product Name;Recommended Browse Nodes;Outer Material Type;Material Composition;Colour Map;Colour;Size;Department;Size Map;Adult Flag;Standard Price;Quantity;Main Image Url;Other Image Url1;Other Image Url2;Other Image Url3;Other Image Url4;Other Image Url5;Other Image Url6;Other Image Url7;Other Image Url8;Parentage;Parent SKU;Relationship Type;Variation Theme;Update Delete;Product Description;Inner Material Type;Product Care Instructions;Model Name;Model Number;Manufacturer Part Number;Product Exemption Reason;Search Terms;Season and collection year;Pattern description;Occasion description;Fitting type;Key Product Features;Key Product Features;Key Product Features;Key Product Features;Key Product Features;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;Season;material_type;Style Name;Sleeve Type;Collar Style;size-modifier;Neck size;Neck Size unit;Shipping Weight;Website Shipping Weight Unit Of Measure;Item Width;Item Height;Item Shape;Item Dimensions Unit Of Measure;Item Length;Fulfillment Centre ID;Package Length;package-width;Package Height;Package Weight;Package Weight Unit Of Measure;Package Dimensions Unit Of Measure;Legal Disclaimer Description;Safety Warning;EU Toys Safety Directive Age-specific warning;EU Toys Safety Directive Non-Age-specific warning;EU Toys Safety Directive language warning;Country/Region Of Origin;Is this product a battery or does it utilise batteries?;Batteries are Included;Battery composition;Battery type/size;Battery type/size;Battery type/size;Number of batteries;Number of batteries;Number of batteries;Battery weight (grams);battery_weight_unit_of_measure;Number of Lithium Metal Cells;Number of Lithium-ion Cells;Lithium Battery Packaging;Watt hours per battery;lithium_battery_energy_content_unit_of_measure;Lithium content (grams);lithium_battery_weight_unit_of_measure;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;UN number;Safety Data Sheet (SDS) URL;Item Weight;item_weight_unit_of_measure;Volume;item_volume_unit_of_measure;Flash point (°C)?;Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Condition Type;condition_note;Currency;Handling Time;Sale Price;Sale From Date;Sale End Date;max-aggregate-ship-quantity;Package Quantity;Number of Items;Can Be Gift Messaged;Is Gift Wrap Available?;Is Discontinued by Manufacturer;Launch Date;Restock Date;Recommended Retail Price;Stop Selling Date;Max Order Quantity;Merchant Shipping Group;Offering Release Date;Scheduled Delivery SKU List;RRP;Product Tax Code;Business Price;Quantity Price Type;Quantity Lower Bound 1;Quantity Price 1;Quantity Lower Bound 2;Quantity Price 2;Quantity Lower Bound 3;Quantity Price 3;Quantity Lower Bound 4;Quantity Price 4;Quantity Lower Bound 5;Quantity Price 5;National Stock Number;United Nations Standard Products and Services Code;Pricing Action\n")
    IT.write(
        "feed_product_type;item_sku;brand_name;external_product_id;external_product_id_type;item_name;recommended_browse_nodes;outer_material_type;material_composition;color_map;color_name;size_name;department_name;size_map;is_adult_product;standard_price;quantity;main_image_url;other_image_url1;other_image_url2;other_image_url3;other_image_url4;other_image_url5;other_image_url6;other_image_url7;other_image_url8;parent_child;parent_sku;relationship_type;variation_theme;update_delete;product_description;inner_material_type;care_instructions;model_name;model;part_number;gtin_exemption_reason;generic_keywords;collection_name;pattern_type;lifestyle;fit_type;bullet_point1;bullet_point2;bullet_point3;bullet_point4;bullet_point5;platinum_keywords1;platinum_keywords2;platinum_keywords3;platinum_keywords4;platinum_keywords5;seasons;material_type;style_name;sleeve_type;collar_style;special_size_type;neck_size;neck_size_unit_of_measure;website_shipping_weight;website_shipping_weight_unit_of_measure;item_width;item_height;item_shape;item_dimensions_unit_of_measure;item_length;fulfillment_center_id;package_length;package_width;package_height;package_weight;package_weight_unit_of_measure;package_dimensions_unit_of_measure;legal_disclaimer_description;safety_warning;eu_toys_safety_directive_age_warning;eu_toys_safety_directive_warning;eu_toys_safety_directive_language;country_of_origin;batteries_required;are_batteries_included;battery_cell_composition;battery_type1;battery_type2;battery_type3;number_of_batteries1;number_of_batteries2;number_of_batteries3;battery_weight;battery_weight_unit_of_measure;number_of_lithium_metal_cells;number_of_lithium_ion_cells;lithium_battery_packaging;lithium_battery_energy_content;lithium_battery_energy_content_unit_of_measure;lithium_battery_weight;lithium_battery_weight_unit_of_measure;supplier_declared_dg_hz_regulation1;supplier_declared_dg_hz_regulation2;supplier_declared_dg_hz_regulation3;supplier_declared_dg_hz_regulation4;supplier_declared_dg_hz_regulation5;hazmat_united_nations_regulatory_id;safety_data_sheet_url;item_weight;item_weight_unit_of_measure;item_volume;item_volume_unit_of_measure;flash_point;ghs_classification_class1;ghs_classification_class2;ghs_classification_class3;condition_type;condition_note;currency;fulfillment_latency;sale_price;sale_from_date;sale_end_date;max_aggregate_ship_quantity;item_package_quantity;number_of_items;offering_can_be_gift_messaged;offering_can_be_giftwrapped;is_discontinued_by_manufacturer;product_site_launch_date;restock_date;list_price;offering_end_date;max_order_quantity;merchant_shipping_group_name;offering_start_date;delivery_schedule_group_id;uvp_list_price;product_tax_code;business_price;quantity_price_type;quantity_lower_bound1;quantity_price1;quantity_lower_bound2;quantity_price2;quantity_lower_bound3;quantity_price3;quantity_lower_bound4;quantity_price4;quantity_lower_bound5;quantity_price5;national_stock_number;unspsc_code;pricing_action\n")
    IT.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    IT.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    ES = open("ES.csv", "x")
    ES.write(
        "TemplateType=fptcustom;Version=2019.0519;TemplateSignature=U0hJUlQ=;The top 3 rows are for Amazon.com use only. Do not modify or delete the top 3 rows.;;;;;;;;;;;;;;;Images;;;;;;;;Variation;;;;Basic;;;;;;;;Discovery;;;;;;;;;;;;;;;;;Product Enrichment;;;;Dimensions;;;;;;;;;Fulfillment;;;;;;;Compliance;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Offer;;;;;;;;;;;;;;;;;;;;;;;b2b;;;;;;;;;;;;;;”)\n")
    ES.write(
        "Product Type;Seller SKU;Brand Name;Product ID;Product ID Type;Product Name;Recommended Browse Nodes;Outer Material Type;Material Composition;Colour Map;Colour;Size;Department;Size Map;Adult Flag;Standard Price;Quantity;Main Image Url;Other Image Url1;Other Image Url2;Other Image Url3;Other Image Url4;Other Image Url5;Other Image Url6;Other Image Url7;Other Image Url8;Parentage;Parent SKU;Relationship Type;Variation Theme;Update Delete;Product Description;Inner Material Type;Product Care Instructions;Model Name;Model Number;Manufacturer Part Number;Product Exemption Reason;Search Terms;Season and collection year;Pattern description;Occasion description;Fitting type;Key Product Features;Key Product Features;Key Product Features;Key Product Features;Key Product Features;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;Season;material_type;Style Name;Sleeve Type;Collar Style;size-modifier;Neck size;Neck Size unit;Shipping Weight;Website Shipping Weight Unit Of Measure;Item Width;Item Height;Item Shape;Item Dimensions Unit Of Measure;Item Length;Fulfillment Centre ID;Package Length;package-width;Package Height;Package Weight;Package Weight Unit Of Measure;Package Dimensions Unit Of Measure;Legal Disclaimer Description;Safety Warning;EU Toys Safety Directive Age-specific warning;EU Toys Safety Directive Non-Age-specific warning;EU Toys Safety Directive language warning;Country/Region Of Origin;Is this product a battery or does it utilise batteries?;Batteries are Included;Battery composition;Battery type/size;Battery type/size;Battery type/size;Number of batteries;Number of batteries;Number of batteries;Battery weight (grams);battery_weight_unit_of_measure;Number of Lithium Metal Cells;Number of Lithium-ion Cells;Lithium Battery Packaging;Watt hours per battery;lithium_battery_energy_content_unit_of_measure;Lithium content (grams);lithium_battery_weight_unit_of_measure;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;UN number;Safety Data Sheet (SDS) URL;Item Weight;item_weight_unit_of_measure;Volume;item_volume_unit_of_measure;Flash point (°C)?;Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Condition Type;condition_note;Currency;Handling Time;Sale Price;Sale From Date;Sale End Date;max-aggregate-ship-quantity;Package Quantity;Number of Items;Can Be Gift Messaged;Is Gift Wrap Available?;Is Discontinued by Manufacturer;Launch Date;Restock Date;Recommended Retail Price;Stop Selling Date;Max Order Quantity;Merchant Shipping Group;Offering Release Date;Scheduled Delivery SKU List;RRP;Product Tax Code;Business Price;Quantity Price Type;Quantity Lower Bound 1;Quantity Price 1;Quantity Lower Bound 2;Quantity Price 2;Quantity Lower Bound 3;Quantity Price 3;Quantity Lower Bound 4;Quantity Price 4;Quantity Lower Bound 5;Quantity Price 5;National Stock Number;United Nations Standard Products and Services Code;Pricing Action\n")
    ES.write(
        "feed_product_type;item_sku;brand_name;external_product_id;external_product_id_type;item_name;recommended_browse_nodes;outer_material_type;material_composition;color_map;color_name;size_name;department_name;size_map;is_adult_product;standard_price;quantity;main_image_url;other_image_url1;other_image_url2;other_image_url3;other_image_url4;other_image_url5;other_image_url6;other_image_url7;other_image_url8;parent_child;parent_sku;relationship_type;variation_theme;update_delete;product_description;inner_material_type;care_instructions;model_name;model;part_number;gtin_exemption_reason;generic_keywords;collection_name;pattern_type;lifestyle;fit_type;bullet_point1;bullet_point2;bullet_point3;bullet_point4;bullet_point5;platinum_keywords1;platinum_keywords2;platinum_keywords3;platinum_keywords4;platinum_keywords5;seasons;material_type;style_name;sleeve_type;collar_style;special_size_type;neck_size;neck_size_unit_of_measure;website_shipping_weight;website_shipping_weight_unit_of_measure;item_width;item_height;item_shape;item_dimensions_unit_of_measure;item_length;fulfillment_center_id;package_length;package_width;package_height;package_weight;package_weight_unit_of_measure;package_dimensions_unit_of_measure;legal_disclaimer_description;safety_warning;eu_toys_safety_directive_age_warning;eu_toys_safety_directive_warning;eu_toys_safety_directive_language;country_of_origin;batteries_required;are_batteries_included;battery_cell_composition;battery_type1;battery_type2;battery_type3;number_of_batteries1;number_of_batteries2;number_of_batteries3;battery_weight;battery_weight_unit_of_measure;number_of_lithium_metal_cells;number_of_lithium_ion_cells;lithium_battery_packaging;lithium_battery_energy_content;lithium_battery_energy_content_unit_of_measure;lithium_battery_weight;lithium_battery_weight_unit_of_measure;supplier_declared_dg_hz_regulation1;supplier_declared_dg_hz_regulation2;supplier_declared_dg_hz_regulation3;supplier_declared_dg_hz_regulation4;supplier_declared_dg_hz_regulation5;hazmat_united_nations_regulatory_id;safety_data_sheet_url;item_weight;item_weight_unit_of_measure;item_volume;item_volume_unit_of_measure;flash_point;ghs_classification_class1;ghs_classification_class2;ghs_classification_class3;condition_type;condition_note;currency;fulfillment_latency;sale_price;sale_from_date;sale_end_date;max_aggregate_ship_quantity;item_package_quantity;number_of_items;offering_can_be_gift_messaged;offering_can_be_giftwrapped;is_discontinued_by_manufacturer;product_site_launch_date;restock_date;list_price;offering_end_date;max_order_quantity;merchant_shipping_group_name;offering_start_date;delivery_schedule_group_id;uvp_list_price;product_tax_code;business_price;quantity_price_type;quantity_lower_bound1;quantity_price1;quantity_lower_bound2;quantity_price2;quantity_lower_bound3;quantity_price3;quantity_lower_bound4;quantity_price4;quantity_lower_bound5;quantity_price5;national_stock_number;unspsc_code;pricing_action\n")
    ES.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    ES.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    UK.close()
    DE.close()
    FR.close()
    IT.close()
    ES.close()

#  ----- DE File ------
def Add(Number, UK_Title, DE_Title, FR_Title, ES_Title, IT_Title, URL, Design_number):
    item_sku = ["VYR BALTA", "MOT BALTA", "VYR PILKA", "MOT PILKA", "VAIK BALTA", "VAIK PILKA", "MEG", "HUD"]
    item_nameIT = ["Uomo Maglietta Bianco Men's White T-shirt Tshirt T shirt Tee",
                    "Donna Maglietta Bianco Women's White T-shirt Tshirt T shirt Tee",
                    "Uomo Maglietta Grigio Men's Grey T-shirt Tshirt T shirt Tee",
                    "Donna Maglietta Grigio Women's Grey T-shirt Tshirt T shirt Tee",
                    "Bambini Unisex Ragazzi Ragazze Maglietta Bianco Kids Boys Girls White T-shirt Tshirt T shirt Tee",
                    "Bambini Unisex Ragazzi Ragazze Maglietta Grigio Kids Boys Girls Grey T-shirt Tshirt T shirt Tee",
                    "Unisex Uomo Donna Maglione Grigio Women's Men's Grey Sweatshirt Pullover",
                    "Unisex Uomo Donna Maglione Grigio Women's Men's Sweatshirt Pullover Hoodie"]
    item_nameES = ["Hombres Camiseta Blanco Men's White T-shirt Tshirt T shirt",
                    "Camiseta Mujer Blanco Women's White T-shirt Tshirt Tshirt",
                    "Hombres Camiseta Gris Men's Grey T-shirt Tshirt T shirt",
                    "Camiseta Mujer Gris Women's Grey T-shirt Tshirt T shirt",
                    "Niños Unisexo Niño Niña Camiseta Blanco Kids Unisex Boys Girls White T-shirt Tshirt T shirt",
                    "Niños Unisexo Niño Niña Camiseta Gris Kids Unisex Boys Girls Grey T-shirt Tshirt T shirt",
                    "Unisexo Hombre Mujer Sudadera Gris Unisex Women's Men's Sweatshirt",
                    "Unisexo Hombre Mujer Sudadera Gris Unisex Women's Men's Sweatshirt Hoodie"]
    item_nameFR = ["Homme T-Shirt Blanc Men's White Tshirt T shirt",
                    "Femme T-Shirt Blanc Women's White T shirt Tshirt",
                    "Homme T-Shirt Gris Men's Grey Tshirt T shirt",
                    "Femme T-Shirt Gris Women's Grey Tshirt T shirt",
                    "Unisexe Garçon Filles T-Shirt Blanc Kids Unisex Boys Girls White T shirt",
                    "Unisexe Garçon Filles T-Shirt Gris Kids Unisex Boys Girls Grey Tshirt T shirt",
                    "Unisexe Homme Femme Sweat-Shirt Jersey Pull-Over Gris Unisex Women's Men's Grey Pullover Sweatshirt",
                    "Unisexe Homme Femme Sweat-Shirt Jersey Pull-Over Gris Unisex Women's Men's Hoodie Pullover Sweatshirt"]
    item_name = ["Men's Mens Men White T-shirt Tshirt T shirt Tee",
                    "Women's Womens Women White T-shirt Tshirt T shirt Tee",
                    "Men's Mens Men Grey T-shirt Tshirt T shirt Tee",
                    "Women's Womens Women Grey T-shirt Tshirt T shirt Tee",
                    "Children Kids Unisex Boys Girls White T-shirt Tshirt T shirt Tee",
                    "Children Kids Unisex Boys Girls Grey T-shirt Tshirt T shirt Tee",
                    "Unisex Women Men Sweatshirt Pullover",
                    "Unisex Women Men Sweatshirt Pullover Hoodie"]
    item_nameDE = [" Herren Weiß T-Shirt Men's White Tshirt T shirt Tee",
                    "Damen Weiß T-Shirt Women's White Tshirt T shirt Tee",
                    "Herren Grau T-Shirt Men's Grey T-shirt Tshirt T shirt Tee",
                    "Damen Grau T-Shirt Women's Grey T-shirt Tshirt T shirt Tee",
                    "Unisex Jungen Mädchen Weiß T-Shirt Kids Boys Girls White Tshirt T shirt Tee",
                    "Unisex Jungen Mädchen Grau T-Shirt Kids Boys Girls Grey Tshirt T shirt Tee",
                    "Unisex Herren Damen Grau Jumper Unisex Women's Men's Grey Sweatshirt Pullover",
                    "Unisex Herren Damen Grau Jumper Unisex Women's Men's Sweatshirt Pullover Hoodie"]
    Department = ["Men", "Women", "Men", "Women", "Girls", "Girls", "Men", "Women"]
    recommended_browse_nodes = ["1731028031", "1731502031", "1731028031", "1731502031", "1730918031", "1730918031", "1731021031", "1730980031"]
    recommended_browse_nodesDE = ["1981397031", "1981872031", "1981397031", "1981872031", "1981287031", "1981287031", "1981390031", "1981349031"]
    recommended_browse_nodesFR = ["464806031", "464642031", "464806031", "464642031", "464880031", "464880031", "464812031", "464809031"]
    recommended_browse_nodesES = ["3074182031", "1731502031", "3074182031", "1731502031", "3074353031", "3074353031", "2949377031", "2949376031"]
    recommended_browse_nodesIT = ["2893334031", "2893163031", "2893334031", "2893163031", "2893012031", "2893012031", "3841317031", "3841318031"]
    other_image = ["https://www.dropbox.com/s/tgol170kwehvcb5/MEN%20GUIDE.png?dl=0",
                   "https://www.dropbox.com/s/imtxhums5morg9y/WOMEN%20GUIDE.png?dl=0",
                   "https://www.dropbox.com/s/tgol170kwehvcb5/MEN%20GUIDE.png?dl=0",
                   "https://www.dropbox.com/s/imtxhums5morg9y/WOMEN%20GUIDE.png?dl=0",
                   "https://www.dropbox.com/s/5b498p7xbgxexr8/KIDS%20GUIDE.png?dl=0",
                   "https://www.dropbox.com/s/5b498p7xbgxexr8/KIDS%20GUIDE.png?dl=0",
                   "https://www.dropbox.com/s/4q4y98fugszfvmr/SWEAAT.png?dl=0",
                   "https://www.dropbox.com/s/yzuboo8g879zgog/HODIE.png?dl=0"]
    priceUK = ["10.45", "10.45", "10.45", "10.45", "10.45", "10.45", "24.99", "27.99"]
    price = ["11.99", "11.99", "11.99", "11.99", "11.99", "11.99", "28.99", "30.99"]

    # First line
    UK = open("UK.csv", "a")
    if Number > 5:
        UK.write("sweater;")
    else:
        UK.write("shirt;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" parent;Romexa Tshirt;;GTIN;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";")
    UK.write(recommended_browse_nodes[Number])
    if Number > 5:
        UK.write(";Cotton;70% Cotton 30% Polyester;")
    else:
        UK.write(";Cotton;100% Cotton;")
    if Number <2 or 3 < Number < 5:
        UK.write("White;White;;")
    else:
        UK.write("Grey;Grey;;")
    UK.write(Department[Number])
    UK.write(";;false;")
    UK.write(priceUK[Number])
    UK.write(";5000;")
    UK.write(URL)
    UK.write(";")
    UK.write(other_image[Number])
    UK.write(";;;;;;;;Parent;;;Size;;;;;;;;;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";Spring-Summer 12;;")
    UK.write("Casual;Regular Fit;High quality. Made in EU.; ")
    UK.write("Made by professional silkography method.;Fashionable, stylish, perfect match with any outfit. ;")

    UK.write(";Could be gift for a birthday, Christmas or other celebration, write us!;Will be dispatched by the same day.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;GBP;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Second Line
    if Number > 5:
        UK.write("sweater;")
    else:
        UK.write("shirt;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" ")
    if 3 < Number < 6:
        UK.write("XS")
    else:
        UK.write("S")
    UK.write(";Romexa Tshirt;;GTIN;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";")
    UK.write(recommended_browse_nodes[Number])
    if Number > 5:
        UK.write(";Cotton;70% Cotton 30% Polyester;")
    else:
        UK.write(";Cotton;100% Cotton;")
    if Number <2 or 3 < Number < 5:
        UK.write("White;White;")
    else:
        UK.write("Grey;Grey;")
    if 3 < Number < 6:
        UK.write("XS (110-116cm) (5-6 years);")
    else:
        UK.write("S;")
    UK.write(Department[Number])
    UK.write(";")
    if 3 < Number < 6:
        UK.write("X-Small")
    else:
        UK.write("Small")
    UK.write(";false;")
    UK.write(priceUK[Number])
    UK.write(";5000;")
    UK.write(URL)
    UK.write(";")
    UK.write(other_image[Number])
    UK.write(";;;;;;;;Child;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" parent;Variation;Size;;;;;;;;;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";Spring-Summer 13;;")
    UK.write("Casual;Regular Fit;High quality. Made in EU.; ")
    UK.write("Made by professional silkography method.;Fashionable, stylish, perfect match with any outfit. ;")

    UK.write(";Could be gift for a birthday, Christmas or other celebration, write us!;Will be dispatched by the same day.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;GBP;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    #Third line
    if Number > 5:
        UK.write("sweater;")
    else:
        UK.write("shirt;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" ")
    if 3 < Number < 6:
        UK.write("S")
    else:
        UK.write("M")
    UK.write(";Romexa Tshirt;;GTIN;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";")
    UK.write(recommended_browse_nodes[Number])
    if Number > 5:
        UK.write(";Cotton;70% Cotton 30% Polyester;")
    else:
        UK.write(";Cotton;100% Cotton;")
    if Number <2 or 3 < Number < 5:
        UK.write("White;White;")
    else:
        UK.write("Grey;Grey;")
    if 3 < Number < 6:
        UK.write("S (122-128cm) (7-8 years);")
    else:
        UK.write("M;")
    UK.write(Department[Number])
    UK.write(";")
    if 3 < Number < 6:
        UK.write("Small")
    else:
        UK.write("Medium")
    UK.write(";false;")
    UK.write(priceUK[Number])
    UK.write(";5000;")
    UK.write(URL)
    UK.write(";")
    UK.write(other_image[Number])
    UK.write(";")
    UK.write(";;;;;;;Child;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" parent;Variation;Size;;;;;;;;;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";Spring-Summer 14;;")
    UK.write("Casual;Regular Fit;High quality. Made in EU.; ")
    UK.write("Made by professional silkography method.;Fashionable, stylish, perfect match with any outfit. ;")

    UK.write(";Could be gift for a birthday, Christmas or other celebration, write us!;Will be dispatched by the same day.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;GBP;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Fourth line
    if Number > 5:
        UK.write("sweater;")
    else:
        UK.write("shirt;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" ")
    if 3 < Number < 6:
        UK.write("M")
    else:
        UK.write("L")
    UK.write(";Romexa Tshirt;;GTIN;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";")
    UK.write(recommended_browse_nodes[Number])
    if Number > 5:
        UK.write(";Cotton;70% Cotton 30% Polyester;")
    else:
        UK.write(";Cotton;100% Cotton;")
    if Number < 2 or 3 < Number < 5:
        UK.write("White;White;")
    else:
        UK.write("Grey;Grey;")
    if 3 < Number < 6:
        UK.write("M (134-140cm) (9-10 years);")
    else:
        UK.write("L;")
    UK.write(Department[Number])
    UK.write(";")
    if 3 < Number < 6:
        UK.write("Medium")
    else:
        UK.write("Large")
    UK.write(";false;")
    print(Number)
    UK.write(priceUK[Number])
    UK.write(";5000;")
    UK.write(URL)
    UK.write(";")
    UK.write(other_image[Number])
    UK.write(";;;;;;;;Child;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" parent;Variation;Size;;;;;;;;;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";Spring-Summer 15;;")
    UK.write("Casual;Regular Fit;High quality. Made in EU.; ")
    UK.write("Made by professional silkography method.;Fashionable, stylish, perfect match with any outfit. ;")

    UK.write(";Could be gift for a birthday, Christmas or other celebration, write us!;Will be dispatched by the same day.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;GBP;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Fifth line
    if Number > 5:
        UK.write("sweater;")
    else:
        UK.write("shirt;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" ")
    if 3 < Number < 6:
        UK.write("L")
    else:
        UK.write("XL")
    UK.write(";Romexa Tshirt;;GTIN;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";")
    UK.write(recommended_browse_nodes[Number])
    if Number > 5:
        UK.write(";Cotton;70% Cotton 30% Polyester;")
    else:
        UK.write(";Cotton;100% Cotton;")
    if Number <2 or 3 < Number < 5:
        UK.write("White;White;")
    else:
        UK.write("Grey;Grey;")
    if 3 < Number < 6:
        UK.write("L (146-152cm) (11-12 years);")
    else:
        UK.write("XL;")
    UK.write(Department[Number])
    UK.write(";")
    if 3 < Number < 6:
        UK.write("Large")
    else:
        UK.write("X-Large")
    UK.write(";false;")
    UK.write(priceUK[Number])
    UK.write(";5000;")
    UK.write(URL)
    UK.write(";")
    UK.write(other_image[Number])
    UK.write(";;;;;;;;Child;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" parent;Variation;Size;;;;;;;;;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";Spring-Summer 16;;")
    UK.write("Casual;Regular Fit;High quality. Made in EU.; ")
    UK.write("Made by professional silkography method.;Fashionable, stylish, perfect match with any outfit. ;")

    UK.write(";Could be gift for a birthday, Christmas or other celebration, write us!;Will be dispatched by the same day.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;GBP;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Sixsth line
    if Number > 5:
        UK.write("sweater;")
    else:
        UK.write("shirt;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" ")
    if 3 < Number < 6:
        UK.write("XL")
    else:
        UK.write("XXL")
    UK.write(";Romexa Tshirt;;GTIN;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";")
    UK.write(recommended_browse_nodes[Number])
    if Number > 5:
        UK.write(";Cotton;70% Cotton 30% Polyester;")
    else:
        UK.write(";Cotton;100% Cotton;")
    if Number <2 or 3 < Number < 5:
        UK.write("White;White;")
    else:
        UK.write("Grey;Grey;")
    if 3 < Number < 6:
        UK.write("XL (158-164cm) (12-13 years);")
    else:
        UK.write("XXL;")
    UK.write(Department[Number])
    UK.write(";")
    if 3 < Number < 6:
        UK.write("X-Large")
    else:
        UK.write("XX-Large")
    UK.write(";false;")
    UK.write(priceUK[Number])
    UK.write(";5000;")
    UK.write(URL)
    UK.write(";")
    UK.write(other_image[Number])
    UK.write(";;;;;;;;Child;")
    UK.write (Design_number)
    UK.write(" ")
    UK.write(item_sku[Number])
    UK.write(" parent;Variation;Size;;;;;;;;;")
    UK.write(UK_Title)
    UK.write(" ")
    UK.write(item_name[Number])
    UK.write(";Spring-Summer 17;;")
    UK.write("Casual;Regular Fit;High quality. Made in EU.; ")
    UK.write("Made by professional silkography method.;Fashionable, stylish, perfect match with any outfit. ;")

    UK.write(";Could be gift for a birthday, Christmas or other celebration, write us!;Will be dispatched by the same day.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;GBP;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # End
    UK.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    UK.close()

    #  ---- DE ----

    # First line
    DE = open("DE.csv", "a")
    if Number > 5:
        DE.write("sweater;")
    else:
        DE.write("shirt;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" parent;Romexa Tshirt;;GTIN;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";")
    DE.write(recommended_browse_nodesDE[Number])
    if Number > 5:
        DE.write(";Cotton;70% Baumwolle 30% Polyester;")
    else:
        DE.write(";Cotton;100% Baumwolle;")
    if Number < 2 or 3 < Number < 5:
        DE.write("White;White;;")
    else:
        DE.write("Grey;Grey;;")
    DE.write(Department[Number])
    DE.write(";;false;")
    DE.write(price[Number])
    DE.write(";5000;")
    DE.write(URL)
    DE.write(";")
    DE.write(other_image[Number])
    DE.write(";;;;;;;;Parent;;;Size;;;;;;;;;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";Spring-Summer 12;;")
    DE.write("Casual;Regular Fit;Gute Qualität. In Europa hergestellt. ;")
    DE.write(
        "Hergestellt nach professioneller Seidenmethode.;Modisch, stilvoll, passt perfekt zu jedem Outfit.;")

    DE.write(
        " Könnte ein Geschenk für einen Geburtstag, Weihnachten oder eine andere Feier sein, schreiben Sie uns!;Wird noch am selben Tag versandt. ;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Second Line
    if Number > 5:
        DE.write("sweater;")
    else:
        DE.write("shirt;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" ")
    if 3 < Number < 6:
        DE.write("XS")
    else:
        DE.write("S")
    DE.write(";Romexa Tshirt;;GTIN;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";")
    DE.write(recommended_browse_nodesDE[Number])
    if Number > 5:
        DE.write(";Cotton;70% Baumwolle 30% Polyester;")
    else:
        DE.write(";Cotton;100% Baumwolle;")
    if Number < 2 or 3 < Number < 5:
        DE.write("White;White;")
    else:
        DE.write("Grey;Grey;")
    if 3 < Number < 6:
        DE.write("XS (110-116cm) (5-6 years);")
    else:
        DE.write("S;")
    DE.write(Department[Number])
    DE.write(";")
    if 3 < Number < 6:
        DE.write("X-Small")
    else:
        DE.write("Small")
    DE.write(";false;")
    DE.write(price[Number])
    DE.write(";5000;")
    DE.write(URL)
    DE.write(";")
    DE.write(other_image[Number])
    DE.write(";;;;;;;;Child;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" parent;Variation;Size;;;;;;;;;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";Spring-Summer 13;;")
    DE.write("Casual;Regular Fit;Gute Qualität. In Europa hergestellt. ;")
    DE.write(
        "Hergestellt nach professioneller Seidenmethode.;Modisch, stilvoll, passt perfekt zu jedem Outfit.;")
    DE.write(
        " Könnte ein Geschenk für einen Geburtstag, Weihnachten oder eine andere Feier sein, schreiben Sie uns!;Wird noch am selben Tag versandt. ;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Third line
    if Number > 5:
        DE.write("sweater;")
    else:
        DE.write("shirt;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" ")
    if 3 < Number < 6:
        DE.write("S")
    else:
        DE.write("M")
    DE.write(";Romexa Tshirt;;GTIN;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";")
    DE.write(recommended_browse_nodesDE[Number])
    if Number > 5:
        DE.write(";Cotton;70% Baumwolle 30% Polyester;")
    else:
        DE.write(";Cotton;100% Baumwolle;")
    if Number < 2 or 3 < Number < 5:
        DE.write("White;White;")
    else:
        DE.write("Grey;Grey;")
    if 3 < Number < 6:
        DE.write("S (122-128cm) (7-8 years);")
    else:
        DE.write("M;")
    DE.write(Department[Number])
    DE.write(";")
    if 3 < Number < 6:
        DE.write("Small")
    else:
        DE.write("Medium")
    DE.write(";false;")
    DE.write(price[Number])
    DE.write(";5000;")
    DE.write(URL)
    DE.write(";")
    DE.write(other_image[Number])
    DE.write(";;;;;;;;Child;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" parent;Variation;Size;;;;;;;;;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";Spring-Summer 14;;")
    DE.write("Casual;Regular Fit;Gute Qualität. In Europa hergestellt. ;")
    DE.write(
        "Hergestellt nach professioneller Seidenmethode.;Modisch, stilvoll, passt perfekt zu jedem Outfit.;")
    DE.write(
        " Könnte ein Geschenk für einen Geburtstag, Weihnachten oder eine andere Feier sein, schreiben Sie uns!;Wird noch am selben Tag versandt. ;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Fourth line
    if Number > 5:
        DE.write("sweater;")
    else:
        DE.write("shirt;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" ")
    if 3 < Number < 6:
        DE.write("M")
    else:
        DE.write("L")
    DE.write(";Romexa Tshirt;;GTIN;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";")
    DE.write(recommended_browse_nodesDE[Number])
    if Number > 5:
        DE.write(";Cotton;70% Baumwolle 30% Polyester;")
    else:
        DE.write(";Cotton;100% Baumwolle;")
    if Number < 2 or 3 < Number < 5:
        DE.write("White;White;")
    else:
        DE.write("Grey;Grey;")
    if 3 < Number < 6:
        DE.write("M (134-140cm) (9-10 years);")
    else:
        DE.write("L;")
    DE.write(Department[Number])
    DE.write(";")
    if 3 < Number < 6:
        DE.write("Medium")
    else:
        DE.write("Large")
    DE.write(";false;")
    DE.write(price[Number])
    DE.write(";5000;")
    DE.write(URL)
    DE.write(";")
    DE.write(other_image[Number])
    DE.write(";;;;;;;;Child;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" parent;Variation;Size;;;;;;;;;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";Spring-Summer 15;;")
    DE.write("Casual;Regular Fit;Gute Qualität. In Europa hergestellt. ;")
    DE.write(
        "Hergestellt nach professioneller Seidenmethode.;Modisch, stilvoll, passt perfekt zu jedem Outfit.;")
    DE.write(
        " Könnte ein Geschenk für einen Geburtstag, Weihnachten oder eine andere Feier sein, schreiben Sie uns!;Wird noch am selben Tag versandt. ;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Fifth line
    if Number > 5:
        DE.write("sweater;")
    else:
        DE.write("shirt;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" ")
    if 3 < Number < 6:
        DE.write("L")
    else:
        DE.write("XL")
    DE.write(";Romexa Tshirt;;GTIN;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";")
    DE.write(recommended_browse_nodesDE[Number])
    if Number > 5:
        DE.write(";Cotton;70% Baumwolle 30% Polyester;")
    else:
        DE.write(";Cotton;100% Baumwolle;")
    if Number < 2 or 3 < Number < 5:
        DE.write("White;White;")
    else:
        DE.write("Grey;Grey;")
    if 3 < Number < 6:
        DE.write("L (146-152cm) (11-12 years);")
    else:
        DE.write("XL;")
    DE.write(Department[Number])
    DE.write(";")
    if 3 < Number < 6:
        DE.write("Large")
    else:
        DE.write("X-Large")
    DE.write(";false;")
    DE.write(price[Number])
    DE.write(";5000;")
    DE.write(URL)
    DE.write(";")
    DE.write(other_image[Number])
    DE.write(";;;;;;;;Child;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" parent;Variation;Size;;;;;;;;;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";Spring-Summer 16;;")
    DE.write("Casual;Regular Fit;Gute Qualität. In Europa hergestellt. ;")
    DE.write(
        "Hergestellt nach professioneller Seidenmethode.;Modisch, stilvoll, passt perfekt zu jedem Outfit.;")
    DE.write(
        " Könnte ein Geschenk für einen Geburtstag, Weihnachten oder eine andere Feier sein, schreiben Sie uns!;Wird noch am selben Tag versandt. ;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Sixsth line
    if Number > 5:
        DE.write("sweater;")
    else:
        DE.write("shirt;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" ")
    if 3 < Number < 6:
        DE.write("XL")
    else:
        DE.write("XXL")
    DE.write(";Romexa Tshirt;;GTIN;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";")
    DE.write(recommended_browse_nodesDE[Number])
    if Number > 5:
        DE.write(";Cotton;70% Baumwolle 30% Polyester;")
    else:
        DE.write(";Cotton;100% Baumwolle;")
    if Number < 2 or 3 < Number < 5:
        DE.write("White;White;")
    else:
        DE.write("Grey;Grey;")
    if 3 < Number < 6:
        DE.write("XL (158-164cm) (12-13 years);")
    else:
        DE.write("XXL;")
    DE.write(Department[Number])
    DE.write(";")
    if 3 < Number < 6:
        DE.write("X-Large")
    else:
        DE.write("XX-Large")
    DE.write(";false;")
    DE.write(price[Number])
    DE.write(";5000;")
    DE.write(URL)
    DE.write(";")
    DE.write(other_image[Number])
    DE.write(";;;;;;;;Child;")
    DE.write(Design_number)
    DE.write(" ")
    DE.write(item_sku[Number])
    DE.write(" parent;Variation;Size;;;;;;;;;")
    DE.write(DE_Title)
    DE.write(" ")
    DE.write(item_nameDE[Number])
    DE.write(";Spring-Summer 17;;")
    DE.write("Casual;Regular Fit;Gute Qualität. In Europa hergestellt. ;")
    DE.write(
        "Hergestellt nach professioneller Seidenmethode.;Modisch, stilvoll, passt perfekt zu jedem Outfit.;")
    DE.write(
        " Könnte ein Geschenk für einen Geburtstag, Weihnachten oder eine andere Feier sein, schreiben Sie uns!;Wird noch am selben Tag versandt. ;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # End
    DE.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    DE.close()

    # ---- FR ----
    FR = open("FR.csv", "a")
    if Number > 5:
        FR.write("sweater;")
    else:
        FR.write("shirt;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" parent;Romexa Tshirt;;GTIN;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";")
    FR.write(recommended_browse_nodesFR[Number])
    if Number > 5:
        FR.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        FR.write(";Cotton;100% Algodón;")
    if Number <2 or 3 < Number < 5:
        FR.write("White;White;;")
    else:
        FR.write("Grey;Grey;;")
    FR.write(Department[Number])
    FR.write(";;false;")
    FR.write(price[Number])
    FR.write(";5000;")
    FR.write(URL)
    FR.write(";")
    FR.write(other_image[Number])
    FR.write(";;;;;;;;Parent;;;Size;;;;;;;;;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";Spring-Summer 12;;")
    FR.write("Casual;Regular Fit;Haute qualité. Fabriqué en EU.;")
    FR.write("Fabriqué selon la méthode de la sérographie professionnelle.;À la mode, élégant, match parfait avec n'importe quelle tenue.;Pourrait être un cadeau pour un anniversaire, Noël ou une autre fête, écrivez-nous!;Sera envoyé le même jour;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Second Line
    if Number > 5:
        FR.write("sweater;")
    else:
        FR.write("shirt;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" ")
    if 3 < Number < 6:
        FR.write("XS")
    else:
        FR.write("S")
    FR.write(";Romexa Tshirt;;GTIN;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";")
    FR.write(recommended_browse_nodesFR[Number])
    if Number > 5:
        FR.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        FR.write(";Cotton;100% Algodón;")
    if Number <2 or 3 < Number < 5:
        FR.write("White;White;")
    else:
        FR.write("Grey;Grey;")
    if 3 < Number < 6:
        FR.write("XS (110-116cm) (5-6 years);")
    else:
        FR.write("S;")
    FR.write(Department[Number])
    FR.write(";")
    if 3 < Number < 6:
        FR.write("X-Small")
    else:
        FR.write("Small")
    FR.write(";false;")
    FR.write(price[Number])
    FR.write(";5000;")
    FR.write(URL)
    FR.write(";")
    FR.write(other_image[Number])
    FR.write(";;;;;;;;Child;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" parent;Variation;Size;;;;;;;;;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";Spring-Summer 13;;")
    FR.write("Casual;Regular Fit;Haute qualité. Fabriqué en EU.;")
    FR.write("Fabriqué selon la méthode de la sérographie professionnelle.;À la mode, élégant, match parfait avec n'importe quelle tenue.;Pourrait être un cadeau pour un anniversaire, Noël ou une autre fête, écrivez-nous!;Sera envoyé le même jour;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    #Third line

    if Number > 5:
        FR.write("sweater;")
    else:
        FR.write("shirt;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" ")
    if 3 < Number < 6:
        FR.write("S")
    else:
        FR.write("M")
    FR.write(";Romexa Tshirt;;GTIN;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";")
    FR.write(recommended_browse_nodesFR[Number])
    if Number > 5:
        FR.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        FR.write(";Cotton;100% Algodón;")
    if Number <2 or 3 < Number < 5:
        FR.write("White;White;")
    else:
        FR.write("Grey;Grey;")
    if 3 < Number < 6:
        FR.write("S (122-128cm) (7-8 years);")
    else:
        FR.write("M;")
    FR.write(Department[Number])
    FR.write(";")
    if 3 < Number < 6:
        FR.write("Small")
    else:
        FR.write("Medium")
    FR.write(";false;")
    FR.write(price[Number])
    FR.write(";5000;")
    FR.write(URL)
    FR.write(";")
    FR.write(other_image[Number])
    FR.write(";;;;;;;;Child;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" parent;Variation;Size;;;;;;;;;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";Spring-Summer 14;;")
    FR.write("Casual;Regular Fit;Haute qualité. Fabriqué en EU.;")
    FR.write("Fabriqué selon la méthode de la sérographie professionnelle.;À la mode, élégant, match parfait avec n'importe quelle tenue.;Pourrait être un cadeau pour un anniversaire, Noël ou une autre fête, écrivez-nous!;Sera envoyé le même jour;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # Fourth line

    if Number > 5:
        FR.write("sweater;")
    else:
        FR.write("shirt;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" ")
    if 3 < Number < 6:
        FR.write("M")
    else:
        FR.write("L")
    FR.write(";Romexa Tshirt;;GTIN;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";")
    FR.write(recommended_browse_nodesFR[Number])
    if Number > 5:
        FR.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        FR.write(";Cotton;100% Algodón;")
    if Number < 2 or 3 < Number < 5:
        FR.write("White;White;")
    else:
        FR.write("Grey;Grey;")
    if 3 < Number < 6:
        FR.write("M (134-140cm) (9-10 years);")
    else:
        FR.write("L;")
    FR.write(Department[Number])
    FR.write(";")
    if 3 < Number < 6:
        FR.write("Medium")
    else:
        FR.write("Large")
    FR.write(";false;")
    FR.write(price[Number])
    FR.write(";5000;")
    FR.write(URL)
    FR.write(";")
    FR.write(other_image[Number])
    FR.write(";;;;;;;;Child;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" parent;Variation;Size;;;;;;;;;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";Spring-Summer 15;;")
    FR.write("Casual;Regular Fit;Haute qualité. Fabriqué en EU.;")
    FR.write("Fabriqué selon la méthode de la sérographie professionnelle.;À la mode, élégant, match parfait avec n'importe quelle tenue.;Pourrait être un cadeau pour un anniversaire, Noël ou une autre fête, écrivez-nous!;Sera envoyé le même jour;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # Fifth line

    if Number > 5:
        FR.write("sweater;")
    else:
        FR.write("shirt;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" ")
    if 3 < Number < 6:
        FR.write("L")
    else:
        FR.write("XL")
    FR.write(";Romexa Tshirt;;GTIN;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";")
    FR.write(recommended_browse_nodesFR[Number])
    if Number > 5:
        FR.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        FR.write(";Cotton;100% Algodón;")
    if Number <2 or 3 < Number < 5:
        FR.write("White;White;")
    else:
        FR.write("Grey;Grey;")
    if 3 < Number < 6:
        FR.write("L (146-152cm) (11-12 years);")
    else:
        FR.write("XL;")
    FR.write(Department[Number])
    FR.write(";")
    if 3 < Number < 6:
        FR.write("Large")
    else:
        FR.write("X-Large")
    FR.write(";false;")
    FR.write(price[Number])
    FR.write(";5000;")
    FR.write(URL)
    FR.write(";")
    FR.write(other_image[Number])
    FR.write(";;;;;;;;Child;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" parent;Variation;Size;;;;;;;;;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";Spring-Summer 16;;")
    FR.write("Casual;Regular Fit;Haute qualité. Fabriqué en EU.;")
    FR.write("Fabriqué selon la méthode de la sérographie professionnelle.;À la mode, élégant, match parfait avec n'importe quelle tenue.;Pourrait être un cadeau pour un anniversaire, Noël ou une autre fête, écrivez-nous!;Sera envoyé le même jour;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # Sixsth line

    if Number > 5:
        FR.write("sweater;")
    else:
        FR.write("shirt;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" ")
    if 3 < Number < 6:
        FR.write("XL")
    else:
        FR.write("XXL")
    FR.write(";Romexa Tshirt;;GTIN;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";")
    FR.write(recommended_browse_nodesFR[Number])
    if Number > 5:
        FR.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        FR.write(";Cotton;100% Algodón;")
    if Number <2 or 3 < Number < 5:
        FR.write("White;White;")
    else:
        FR.write("Grey;Grey;")
    if 3 < Number < 6:
        FR.write("XL (158-164cm) (12-13 years);")
    else:
        FR.write("XXL;")
    FR.write(Department[Number])
    FR.write(";")
    if 3 < Number < 6:
        FR.write("X-Large")
    else:
        FR.write("XX-Large")
    FR.write(";false;")
    FR.write(price[Number])
    FR.write(";5000;")
    FR.write(URL)
    FR.write(";")
    FR.write(other_image[Number])
    FR.write(";;;;;;;;Child;")
    FR.write (Design_number)
    FR.write(" ")
    FR.write(item_sku[Number])
    FR.write(" parent;Variation;Size;;;;;;;;;")
    FR.write(FR_Title)
    FR.write(" ")
    FR.write(item_nameFR[Number])
    FR.write(";Spring-Summer 17;;")
    FR.write("Casual;Regular Fit;Haute qualité. Fabriqué en EU.;")
    FR.write("Fabriqué selon la méthode de la sérographie professionnelle.;À la mode, élégant, match parfait avec n'importe quelle tenue.;Pourrait être un cadeau pour un anniversaire, Noël ou une autre fête, écrivez-nous!;Sera envoyé le même jour;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # End
    FR.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    FR.close()

    # ---- ES ----
    # First line
    ES = open("ES.csv", "a")
    if Number > 5:
        ES.write("sweater;")
    else:
        ES.write("shirt;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" parent;Romexa Tshirt;;GTIN;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";")
    ES.write(recommended_browse_nodesES[Number])
    if Number > 5:
        ES.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        ES.write(";Cotton;100% Algodón;")
    if Number < 2 or 3 < Number < 5:
        ES.write("White;White;;")
    else:
        ES.write("Grey;Grey;;")
    ES.write(Department[Number])
    ES.write(";;false;")
    ES.write(price[Number])
    ES.write(";5000;")
    ES.write(URL)
    ES.write(";")
    ES.write(other_image[Number])
    ES.write(";;;;;;;;Parent;;;Size;;;;;;;;;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";Spring-Summer 12;;")
    ES.write(
            "Casual;Regular Fit;Alta calidad. Fabricado en la EU.; ")
    ES.write(
        "Realizado por el método profesional de la seda.;Moda, estilo, combinación perfecta con cualquier atuendo.;Podría ser un regalo para un cumpleaños, navidad u otra celebración, escríbenos!;Será enviado el mismo día.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Second Line
    if Number > 5:
        ES.write("sweater;")
    else:
        ES.write("shirt;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" ")
    if 3 < Number < 6:
        ES.write("XS")
    else:
        ES.write("S")
    ES.write(";Romexa Tshirt;;GTIN;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";")
    ES.write(recommended_browse_nodesES[Number])
    if Number > 5:
        ES.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        ES.write(";Cotton;100% Algodón;")
    if Number < 2 or 3 < Number < 5:
        ES.write("White;White;")
    else:
        ES.write("Grey;Grey;")
    if 3 < Number < 6:
        ES.write("XS (110-116cm) (5-6 years);")
    else:
        ES.write("S;")
    ES.write(Department[Number])
    ES.write(";")
    if 3 < Number < 6:
        ES.write("X-Small")
    else:
        ES.write("Small")
    ES.write(";false;")
    ES.write(price[Number])
    ES.write(";5000;")
    ES.write(URL)
    ES.write(";")
    ES.write(other_image[Number])
    ES.write(";;;;;;;;Child;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" parent;Variation;Size;;;;;;;;;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";Spring-Summer 13;;")
    ES.write(
            "Casual;Regular Fit;Alta calidad. Fabricado en la EU.; ")
    ES.write(
        "Realizado por el método profesional de la seda.;Moda, estilo, combinación perfecta con cualquier atuendo.;Podría ser un regalo para un cumpleaños, navidad u otra celebración, escríbenos!;Será enviado el mismo día.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # Third line
    if Number > 5:
        ES.write("sweater;")
    else:
        ES.write("shirt;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" ")
    if 3 < Number < 6:
        ES.write("S")
    else:
        ES.write("M")
    ES.write(";Romexa Tshirt;;GTIN;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";")
    ES.write(recommended_browse_nodesES[Number])
    if Number > 5:
        ES.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        ES.write(";Cotton;100% Algodón;")
    if Number < 2 or 3 < Number < 5:
        ES.write("White;White;")
    else:
        ES.write("Grey;Grey;")
    if 3 < Number < 6:
        ES.write("S (122-128cm) (7-8 years);")
    else:
        ES.write("M;")
    ES.write(Department[Number])
    ES.write(";")
    if 3 < Number < 6:
        ES.write("Small")
    else:
        ES.write("Medium")
    ES.write(";false;")
    ES.write(price[Number])
    ES.write(";5000;")
    ES.write(URL)
    ES.write(";")
    ES.write(other_image[Number])
    ES.write(";;;;;;;;Child;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" parent;Variation;Size;;;;;;;;;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";Spring-Summer 14;;")
    ES.write(
            "Casual;Regular Fit;Alta calidad. Fabricado en la EU.; ")
    ES.write(
        "Realizado por el método profesional de la seda.;Moda, estilo, combinación perfecta con cualquier atuendo.;Podría ser un regalo para un cumpleaños, navidad u otra celebración, escríbenos!;Será enviado el mismo día.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # Fourth line
    if Number > 5:
        ES.write("sweater;")
    else:
        ES.write("shirt;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" ")
    if 3 < Number < 6:
        ES.write("M")
    else:
        ES.write("L")
    ES.write(";Romexa Tshirt;;GTIN;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";")
    ES.write(recommended_browse_nodesES[Number])
    if Number > 5:
        ES.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        ES.write(";Cotton;100% Algodón;")
    if Number < 2 or 3 < Number < 5:
        ES.write("White;White;")
    else:
        ES.write("Grey;Grey;")
    if 3 < Number < 6:
        ES.write("M (134-140cm) (9-10 years);")
    else:
        ES.write("L;")
    ES.write(Department[Number])
    ES.write(";")
    if 3 < Number < 6:
        ES.write("Medium")
    else:
        ES.write("Large")
    ES.write(";false;")
    ES.write(price[Number])
    ES.write(";5000;")
    ES.write(URL)
    ES.write(";")
    ES.write(other_image[Number])
    ES.write(";;;;;;;;Child;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" parent;Variation;Size;;;;;;;;;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";Spring-Summer 15;;")
    ES.write(
            "Casual;Regular Fit;Alta calidad. Fabricado en la EU.; ")
    ES.write(
        "Realizado por el método profesional de la seda.;Moda, estilo, combinación perfecta con cualquier atuendo.;Podría ser un regalo para un cumpleaños, navidad u otra celebración, escríbenos!;Será enviado el mismo día.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # Fifth line
    if Number > 5:
        ES.write("sweater;")
    else:
        ES.write("shirt;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" ")
    if 3 < Number < 6:
        ES.write("L")
    else:
        ES.write("XL")
    ES.write(";Romexa Tshirt;;GTIN;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";")
    ES.write(recommended_browse_nodesES[Number])
    if Number > 5:
        ES.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        ES.write(";Cotton;100% Algodón;")
    if Number < 2 or 3 < Number < 5:
        ES.write("White;White;")
    else:
        ES.write("Grey;Grey;")
    if 3 < Number < 6:
        ES.write("L (146-152cm) (11-12 years);")
    else:
        ES.write("XL;")
    ES.write(Department[Number])
    ES.write(";")
    if 3 < Number < 6:
        ES.write("Large")
    else:
        ES.write("X-Large")
    ES.write(";false;")
    ES.write(price[Number])
    ES.write(";5000;")
    ES.write(URL)
    ES.write(";")
    ES.write(other_image[Number])
    ES.write(";;;;;;;;Child;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" parent;Variation;Size;;;;;;;;;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";Spring-Summer 16;;")
    ES.write(
            "Casual;Regular Fit;Alta calidad. Fabricado en la EU.; ")
    ES.write(
        "Realizado por el método profesional de la seda.;Moda, estilo, combinación perfecta con cualquier atuendo.;Podría ser un regalo para un cumpleaños, navidad u otra celebración, escríbenos!;Será enviado el mismo día.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # Sixsth line
    if Number > 5:
        ES.write("sweater;")
    else:
        ES.write("shirt;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" ")
    if 3 < Number < 6:
        ES.write("XL")
    else:
        ES.write("XXL")
    ES.write(";Romexa Tshirt;;GTIN;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";")
    ES.write(recommended_browse_nodesES[Number])
    if Number > 5:
        ES.write(";Cotton;70% Algodón 30% Poliéster;")
    else:
        ES.write(";Cotton;100% Algodón;")
    if Number < 2 or 3 < Number < 5:
        ES.write("White;White;")
    else:
        ES.write("Grey;Grey;")
    if 3 < Number < 6:
        ES.write("XL (158-164cm) (12-13 years);")
    else:
        ES.write("XXL;")
    ES.write(Department[Number])
    ES.write(";")
    if 3 < Number < 6:
        ES.write("X-Large")
    else:
        ES.write("XX-Large")
    ES.write(";false;")
    ES.write(price[Number])
    ES.write(";5000;")
    ES.write(URL)
    ES.write(";")
    ES.write(other_image[Number])
    ES.write(";;;;;;;;Child;")
    ES.write(Design_number)
    ES.write(" ")
    ES.write(item_sku[Number])
    ES.write(" parent;Variation;Size;;;;;;;;;")
    ES.write(ES_Title)
    ES.write(" ")
    ES.write(item_nameES[Number])
    ES.write(";Spring-Summer 17;;")
    ES.write(
            "Casual;Regular Fit;Alta calidad. Fabricado en la EU.; ")
    ES.write(
        "Realizado por el método profesional de la seda.;Moda, estilo, combinación perfecta con cualquier atuendo.;Podría ser un regalo para un cumpleaños, navidad u otra celebración, escríbenos!;Será enviado el mismo día.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # End
    ES.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    ES.close()

    # ---- IT -----

    IT = open("IT.csv", "a")
    if Number > 5:
        IT.write("sweater;")
    else:
        IT.write("shirt;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" parent;Romexa Tshirt;;GTIN;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";")
    IT.write(recommended_browse_nodesIT[Number])
    if Number > 5:
        IT.write(";Cotton;70% Cotone 30% Poliestere;")
    else:
        IT.write(";Cotton;100% Cotone;")
    if Number < 2 or 3 < Number < 5:
        IT.write("White;White;;")
    else:
        IT.write("Grey;Grey;;")
    IT.write(Department[Number])
    IT.write(";;false;")
    IT.write(price[Number])
    IT.write(";5000;")
    IT.write(URL)
    IT.write(";")
    IT.write(other_image[Number])
    IT.write(";;;;;;;;Parent;;;Size;;;;;;;;;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";Spring-Summer 12;;")
    IT.write("Casual;Regular Fit;Realizzato con il metodo della silkografia professionale.; ")
    IT.write(
        "Realizzato con il metodo della silkografia professionale.;Abbinabile alla moda, elegante, perfetto con qualsiasi outfit.;Potrebbe essere un regalo per un compleanno, Natale o altre celebrazioni, scrivici!;Sarà spedito dallo stesso giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # Second Line
    if Number > 5:
        IT.write("sweater;")
    else:
        IT.write("shirt;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" ")
    if 3 < Number < 6:
        IT.write("XS")
    else:
        IT.write("S")
    IT.write(";Romexa Tshirt;;GTIN;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";")
    IT.write(recommended_browse_nodesIT[Number])
    if Number > 5:
        IT.write(";Cotton;70% Cotone 30% Poliestere;")
    else:
        IT.write(";Cotton;100% Cotone;")
    if Number < 2 or 3 < Number < 5:
        IT.write("White;White;")
    else:
        IT.write("Grey;Grey;")
    if 3 < Number < 6:
        IT.write("XS (110-116cm) (5-6 years);")
    else:
        IT.write("S;")
    IT.write(Department[Number])
    IT.write(";")
    if 3 < Number < 6:
        IT.write("X-Small")
    else:
        IT.write("Small")
    IT.write(";false;")
    IT.write(price[Number])
    IT.write(";5000;")
    IT.write(URL)
    IT.write(";")
    IT.write(other_image[Number])
    IT.write(";;;;;;;;Child;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" parent;Variation;Size;;;;;;;;;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";Spring-Summer 13;;")
    IT.write("Casual;Regular Fit;Realizzato con il metodo della silkografia professionale.; ")
    IT.write(
        "Realizzato con il metodo della silkografia professionale.;Abbinabile alla moda, elegante, perfetto con qualsiasi outfit.;Potrebbe essere un regalo per un compleanno, Natale o altre celebrazioni, scrivici!;Sarà spedito dallo stesso giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Third line
    if Number > 5:
        IT.write("sweater;")
    else:
        IT.write("shirt;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" ")
    if 3 < Number < 6:
        IT.write("S")
    else:
        IT.write("M")
    IT.write(";Romexa Tshirt;;GTIN;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";")
    IT.write(recommended_browse_nodesIT[Number])
    if Number > 5:
        IT.write(";Cotton;70% Cotone 30% Poliestere;")
    else:
        IT.write(";Cotton;100% Cotone;")
    if Number < 2 or 3 < Number < 5:
        IT.write("White;White;")
    else:
        IT.write("Grey;Grey;")
    if 3 < Number < 6:
        IT.write("S (122-128cm) (7-8 years);")
    else:
        IT.write("M;")
    IT.write(Department[Number])
    IT.write(";")
    if 3 < Number < 6:
        IT.write("Small")
    else:
        IT.write("Medium")
    IT.write(";false;")
    IT.write(price[Number])
    IT.write(";5000;")
    IT.write(URL)
    IT.write(";")
    IT.write(other_image[Number])
    IT.write(";;;;;;;;Child;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" parent;Variation;Size;;;;;;;;;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";Spring-Summer 14;;")
    IT.write("Casual;Regular Fit;Realizzato con il metodo della silkografia professionale.; ")
    IT.write(
        "Realizzato con il metodo della silkografia professionale.;Abbinabile alla moda, elegante, perfetto con qualsiasi outfit.;Potrebbe essere un regalo per un compleanno, Natale o altre celebrazioni, scrivici!;Sarà spedito dallo stesso giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Fourth line
    if Number > 5:
        IT.write("sweater;")
    else:
        IT.write("shirt;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" ")
    if 3 < Number < 6:
        IT.write("M")
    else:
        IT.write("L")
    IT.write(";Romexa Tshirt;;GTIN;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";")
    IT.write(recommended_browse_nodesIT[Number])
    if Number > 5:
        IT.write(";Cotton;70% Cotone 30% Poliestere;")
    else:
        IT.write(";Cotton;100% Cotone;")
    if Number < 2 or 3 < Number < 5:
        IT.write("White;White;")
    else:
        IT.write("Grey;Grey;")
    if 3 < Number < 6:
        IT.write("M (134-140cm) (9-10 years);")
    else:
        IT.write("L;")
    IT.write(Department[Number])
    IT.write(";")
    if 3 < Number < 6:
        IT.write("Medium")
    else:
        IT.write("Large")
    IT.write(";false;")
    IT.write(price[Number])
    IT.write(";5000;")
    IT.write(URL)
    IT.write(";")
    IT.write(other_image[Number])
    IT.write(";;;;;;;;Child;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" parent;Variation;Size;;;;;;;;;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";Spring-Summer 15;;")
    IT.write("Casual;Regular Fit;Realizzato con il metodo della silkografia professionale.; ")
    IT.write(
        "Realizzato con il metodo della silkografia professionale.;Abbinabile alla moda, elegante, perfetto con qualsiasi outfit.;Potrebbe essere un regalo per un compleanno, Natale o altre celebrazioni, scrivici!;Sarà spedito dallo stesso giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")

    # Fifth line
    if Number > 5:
        IT.write("sweater;")
    else:
        IT.write("shirt;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" ")
    if 3 < Number < 6:
        IT.write("L")
    else:
        IT.write("XL")
    IT.write(";Romexa Tshirt;;GTIN;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";")
    IT.write(recommended_browse_nodesIT[Number])
    if Number > 5:
        IT.write(";Cotton;70% Cotone 30% Poliestere;")
    else:
        IT.write(";Cotton;100% Cotone;")
    if Number < 2 or 3 < Number < 5:
        IT.write("White;White;")
    else:
        IT.write("Grey;Grey;")
    if 3 < Number < 6:
        IT.write("L (146-152cm) (11-12 years);")
    else:
        IT.write("XL;")
    IT.write(Department[Number])
    IT.write(";")
    if 3 < Number < 6:
        IT.write("Large")
    else:
        IT.write("X-Large")
    IT.write(";false;")
    IT.write(price[Number])
    IT.write(";5000;")
    IT.write(URL)
    IT.write(";")
    IT.write(other_image[Number])
    IT.write(";;;;;;;;Child;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" parent;Variation;Size;;;;;;;;;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";Spring-Summer 16;;")
    IT.write("Casual;Regular Fit;Realizzato con il metodo della silkografia professionale.; ")
    IT.write(
        "Realizzato con il metodo della silkografia professionale.;Abbinabile alla moda, elegante, perfetto con qualsiasi outfit.;Potrebbe essere un regalo per un compleanno, Natale o altre celebrazioni, scrivici!;Sarà spedito dallo stesso giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # Sixsth line
    if Number > 5:
        IT.write("sweater;")
    else:
        IT.write("shirt;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" ")
    if 3 < Number < 6:
        IT.write("XL")
    else:
        IT.write("XXL")
    IT.write(";Romexa Tshirt;;GTIN;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";")
    IT.write(recommended_browse_nodesIT[Number])
    if Number > 5:
        IT.write(";Cotton;70% Cotone 30% Poliestere;")
    else:
        IT.write(";Cotton;100% Cotone;")
    if Number < 2 or 3 < Number < 5:
        IT.write("White;White;")
    else:
        IT.write("Grey;Grey;")
    if 3 < Number < 6:
        IT.write("XL (158-164cm) (12-13 years);")
    else:
        IT.write("XXL;")
    IT.write(Department[Number])
    IT.write(";")
    if 3 < Number < 6:
        IT.write("X-Large")
    else:
        IT.write("XX-Large")
    IT.write(";false;")
    IT.write(price[Number])
    IT.write(";5000;")
    IT.write(URL)
    IT.write(";")
    IT.write(other_image[Number])
    IT.write(";;;;;;;;Child;")
    IT.write(Design_number)
    IT.write(" ")
    IT.write(item_sku[Number])
    IT.write(" parent;Variation;Size;;;;;;;;;")
    IT.write(IT_Title)
    IT.write(" ")
    IT.write(item_nameIT[Number])
    IT.write(";Spring-Summer 17;;")
    IT.write("Casual;Regular Fit;Realizzato con il metodo della silkografia professionale.; ")
    IT.write(
        "Realizzato con il metodo della silkografia professionale.;Abbinabile alla moda, elegante, perfetto con qualsiasi outfit.;Potrebbe essere un regalo per un compleanno, Natale o altre celebrazioni, scrivici!;Sarà spedito dallo stesso giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;EUR;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    # End
    IT.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    IT.close()

def EndLine():

    UK = open("UK.csv", "a")
    UK.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    UK.close()

    DE = open("DE.csv", "a")
    DE.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    DE.close()

    FR = open("FR.csv", "a")
    FR.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    FR.close()

    IT = open("IT.csv", "a")
    IT.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    IT.close()

    ES = open("ES.csv", "a")
    ES.write(
        ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n")
    ES.close()