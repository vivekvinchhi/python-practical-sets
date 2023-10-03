a = "apple"
b = "banana"
para = "In a bustling fruit market, the vibrant colors of apple and banana caught the eye of passersby. A pyramid of crisp, red apple stood tall, their glossy skins glistening in the sunlight. Nearby, clusters of ripe banana hung from a wooden stand, their cheerful yellow peels promising a sweet and creamy delight. As shoppers meandered through the aisles, the fragrance of apple and banana intertwined, creating an irresistible aroma that beckoned them to savor the delicious flavors of these two beloved fruits. Whether it was the juicy bite of a crisp apple or the smooth sweetness of a ripe banana, there was no denying the irresistible appeal of these fruits in their various forms - from apple pies to banana smoothies, they offered a world of culinary possibilities banana."
pl = len(para)
al=len(a)
bl=len(b)
print(pl)
count_a = 0
count_b = 0
i = 0
while i < pl:
    x = para.find(a,i)
    if x == -1:
        break
    count_a = count_a+1
    i = x+al
i = 0
count_a = 0
for _ in range(pl):
    x = para.find(a,i)
    if x == -1:
        break
    count_a = count_a+1
    i = x+al
    

i=0
while i < pl:
    x = para.find(b,i)
    if x == -1:
        break
    count_b = count_b+1
    i = x+bl

print("Count of ",a,"is : ",count_a)
print("Count of ",b,"is : ",count_b)