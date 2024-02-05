# Wardrobify

Team:

* William Reeves - Shoes
* Chris Sleeger - Hats

## Design

## Shoes microservice

The Shoes microservice is responsible for managing shoe-related data within the application. It consists of models to represent different aspects of shoes and integrates with the Wardrobe microservice to handle relationships with wardrobe items.

Shoe Model: Represents individual shoes and contains attributes such as manufacturer, model name, color, and picture URL. Additionally, it has a foreign key relationship with the BinVO model to specify the storage bin in the wardrobe where the shoe is stored.

BinVO Model: Represents storage bins within the wardrobe. It contains attributes such as import href, closet name, bin number, and bin size. The BinVO model helps organize and categorize shoes within the wardrobe.

## Hats microservice

Explain your models and integration with the wardrobe
microservice, here.

The Hat resource will track the type of fabric, the style name, color, URL for a picture and the location in the wardrobe where the hat exists.
