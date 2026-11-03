products = float(input("Products value: "))
city = input("City: ")
weight = float(input("Weight (kg): "))
coupon = input("Coupon (leave empty if none): ")

# أشيل المسافات وأخلي الحروف سمول
city = city.strip().lower()
coupon = coupon.strip().lower()

# الرياض 15، جدة أو الدمام 20، وأي مدينة ثانية 30
if city == "riyadh":
    shipping = 15
elif city == "jeddah" or city == "dammam":
    shipping = 20
else:
    shipping = 30

# لو الوزن فوق 5 كجم أضيف 2 ريال لكل كيلو زائد
if weight > 5:
    shipping = shipping + (weight - 5) * 2

# الكوبون: tf10 يخصم 10% بس لو المنتجات 100 أو أكثر
discount = 0
if coupon == "tf10":
    if products >= 100:
        discount = products * 0.10
    else:
        print("TF10 not applied: products value must be at least 100 SAR")
elif coupon == "freeship":
    shipping = 0
elif coupon != "":
    print("Invalid coupon")

after_discount = products - discount

# لو المنتجات بعد الخصم 300 أو أكثر الشحن مجاني
if after_discount >= 300:
    shipping = 0

# الضريبة 15% على (المنتجات بعد الخصم + الشحن)
vat = (after_discount + shipping) * 0.15
total = after_discount + shipping + vat

print(f"Products value: {products:.0f}")
print(f"City: {city}")
print(f"Weight (kg): {weight}")
print(f"Coupon: {coupon}")
print(f"Products after discount: {after_discount:.2f} SAR")
print(f"Shipping: {shipping:.2f} SAR")
print(f"VAT: {vat:.2f} SAR")
print(f"Total: {total:.2f} SAR")