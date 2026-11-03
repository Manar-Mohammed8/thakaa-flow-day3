# المهمة 1: منطق الشروط والنصوص

## 1. جدول التوقعات

```python
email = "  Sara.Ahmed@TFCO.SA "
clean = email.strip()
print(clean.lower())
print(email.count("a"), clean.lower().count("a"))
print("tfco" in email, "tfco" in clean.lower())
print(clean.startswith("sara"))
print(len(email), len(clean))
print(clean[:4], clean[-2:])
```

| السطر | توقعي | الناتج الفعلي | سبب الاختلاف |
|---|---|---|---|
| print(clean.lower()) | الإيميل كله بحروف صغيرة | sara.ahmed@tfco.sa | لا يوجد اختلاف |
| print(email.count("a"), clean.lower().count("a")) | 2 و 4 | 2 4 | لا يوجد اختلاف |
| print("tfco" in email, "tfco" in clean.lower()) | False ثم True | False True | لا يوجد اختلاف |
| print(clean.startswith("sara")) | False | False | لا يوجد اختلاف |
| print(len(email), len(clean)) | 20 و 18 | 21 18 | عدّيت مسافتين بدل 3 في أطراف email، فنقص حرف واحد |
| print(clean[:4], clean[-2:]) | Sara و SA | Sara SA | لا يوجد اختلاف |

## 2. ترتيب elif

**ليش ما يطبع Excellent؟**
لأن الدرجة 95 تحقق الشرط الأول `score >= 60`، فيطبع `Pass`، وبايثون يوقف عند أول شرط صحيح وما يكمل باقي شروط `elif`.

**الكود بعد التصحيح:**

```python
score = 95
if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
```

**القاعدة:** نرتّب الشروط من الأعلى إلى الأقل، أو من الأكثر تحديدًا إلى الأقل تحديدًا، عشان شرط عام ما يمنع الشروط اللي بعده من التنفيذ.

## 3. الحساب اليدوي (x = 7)

| السطر | خطوات الحل بيدي | توقعي | الناتج الفعلي |
|---|---|---|---|
| `x > 3 and x % 2 == 0` | True and True | True | False |
| `not (x < 2) or x == 6` | True or False | True | True |
| `x * 2 >= 7 and not x == 5` | True and True | False | True |

**سبب الاختلاف:** في السطر الأول `7 % 2` يعطي 1 مو 0، فالشرط الثاني `False` والنتيجة `False`. وفي السطر الثالث الجزئين `True`، فالنتيجة `True` مو `False`. كنت أنسى أفصل الشرط إلى أجزاء وأحسب كل جزء لحاله قبل النتيجة. وتعلمت أن `and` يحتاج الشرطين `True`، وأن `not` تعكس النتيجة.

## 4. موقف من العمل

نستخدم `strip()` و`lower()` لحذف المسافات وتوحيد الحروف الكبيرة والصغيرة،
فتكون مقارنة اسم المستخدم أدق ولا نرفض مستخدمًا بسبب مسافة أو حرف كبير.
أما كلمة المرور فلازم تفرّق بين الحروف الكبيرة والصغيرة،
وتطبيق `lower()` عليها يقلل الأمان ويقبل كلمات مرور غير صحيحة.