from django.db import models

from .measurement import measurement

class climatic_SensorType(models.Model):
    typee = models.CharField(max_length=100)

    def __str__(self):
        return str(self.typee)

class climatic_SensorTypeList(models.Model):
    name_list = models.CharField(max_length=500)
    typee1 =  models.ForeignKey(climatic_SensorType, related_name='das')
    typee2 =  models.ForeignKey(climatic_SensorType, related_name='da431s')
    typee3 =  models.ForeignKey(climatic_SensorType, related_name="Non1234e")
    typee4 =  models.ForeignKey(climatic_SensorType, related_name="No234577456ne")
    typee5 =  models.ForeignKey(climatic_SensorType, related_name="No235ne")
    typee6 =  models.ForeignKey(climatic_SensorType, related_name="Nogebrene")
    typee7 =  models.ForeignKey(climatic_SensorType, related_name="Noyvfbne")
    typee8 =  models.ForeignKey(climatic_SensorType, related_name="Nowerwene")
    typee9 =  models.ForeignKey(climatic_SensorType, related_name="Noqwrwerne")
    typee10 = models.ForeignKey(climatic_SensorType, related_name="Norrqrne")
    typee11 = models.ForeignKey(climatic_SensorType, related_name="Nobzbzbanifne")
    typee12 = models.ForeignKey(climatic_SensorType, related_name="Nosdfgdsne")
    typee13 = models.ForeignKey(climatic_SensorType, related_name="Nxcbone")
    typee14 = models.ForeignKey(climatic_SensorType, related_name="Nonhrzne")
    typee15 = models.ForeignKey(climatic_SensorType, related_name="Non7575e")
    typee16 = models.ForeignKey(climatic_SensorType, related_name="No4538ne")
    typee17 = models.ForeignKey(climatic_SensorType, related_name="No98689ne")
    typee18 = models.ForeignKey(climatic_SensorType, related_name="No7287ne")
    typee19 = models.ForeignKey(climatic_SensorType, related_name="No45ne")
    typee20 = models.ForeignKey(climatic_SensorType, related_name="Nonecrwe")
    typee21 = models.ForeignKey(climatic_SensorType, related_name="Nocercne")
    typee22 = models.ForeignKey(climatic_SensorType, related_name="Nsgnetzbone")
    typee23 = models.ForeignKey(climatic_SensorType, related_name="Nwertone")
    typee24 = models.ForeignKey(climatic_SensorType, related_name="Nsdfgone")
    typee25 = models.ForeignKey(climatic_SensorType, related_name="Noxvne")
    typee26 = models.ForeignKey(climatic_SensorType, related_name="Nonss78698756645ge")
    typee27 = models.ForeignKey(climatic_SensorType, related_name="Nlkljkjsfhone")
    typee28 = models.ForeignKey(climatic_SensorType, related_name="Nonwerge")
    typee29 = models.ForeignKey(climatic_SensorType, related_name="Nonhte")
    typee30 = models.ForeignKey(climatic_SensorType, related_name="Nonasdfe")
    typee31 = models.ForeignKey(climatic_SensorType, related_name="Nunztone")
    typee32 = models.ForeignKey(climatic_SensorType, related_name="Nonsdrgeegcrtgfge")
    typee33 = models.ForeignKey(climatic_SensorType, related_name="Nosdsdsdsdsddfgne")
    typee34 = models.ForeignKey(climatic_SensorType, related_name="Non235234e")
    typee35 = models.ForeignKey(climatic_SensorType, related_name="No46484ne")
    typee36 = models.ForeignKey(climatic_SensorType, related_name="No523156ne")
    typee37 = models.ForeignKey(climatic_SensorType, related_name="No45684ne")
    typee38 = models.ForeignKey(climatic_SensorType, related_name="Nokiysdne")
    typee39 = models.ForeignKey(climatic_SensorType, related_name="No4684ne")
    typee40 = models.ForeignKey(climatic_SensorType, related_name="Noxcvbxcne")
    typee41 = models.ForeignKey(climatic_SensorType, related_name="Nofghne")
    typee42 = models.ForeignKey(climatic_SensorType, related_name="Nonfgne")
    typee43 = models.ForeignKey(climatic_SensorType, related_name="Nosdfne")
    typee44 = models.ForeignKey(climatic_SensorType, related_name="Nonsdfe")
    typee45 = models.ForeignKey(climatic_SensorType, related_name="Nxcvbone")
    typee46 = models.ForeignKey(climatic_SensorType, related_name="Nosdfgnesdf")
    typee47 = models.ForeignKey(climatic_SensorType, related_name="Noyssdfgne")
    typee48 = models.ForeignKey(climatic_SensorType, related_name="Nosdfgnesdfgne")
    typee49 = models.ForeignKey(climatic_SensorType, related_name="Noddsdfgne")
    typee50 = models.ForeignKey(climatic_SensorType, related_name="Nosdfgne")
    typee51 = models.ForeignKey(climatic_SensorType, related_name="Nasfone")
    typee52 = models.ForeignKey(climatic_SensorType, related_name="Nonrewfe")
    typee53 = models.ForeignKey(climatic_SensorType, related_name="Noerfne")
    typee54 = models.ForeignKey(climatic_SensorType, related_name="Nonasde")
    typee55 = models.ForeignKey(climatic_SensorType, related_name="Nonyxcve")
    typee56 = models.ForeignKey(climatic_SensorType, related_name="Nonfghjfe")
    typee57 = models.ForeignKey(climatic_SensorType, related_name="Nonjke")
    typee58 = models.ForeignKey(climatic_SensorType, related_name="Nonasfve")
    typee59 = models.ForeignKey(climatic_SensorType, related_name="Nonefdghdfgh")
    typee60 = models.ForeignKey(climatic_SensorType, related_name="Nasdasdfa")

    def __str__(self):
        return str(self.name_list)

class climatic_SensorMax(models.Model):
    name_list = models.CharField(max_length=500)
    max1 =  models.DecimalField(max_digits=6, decimal_places=2)
    max2 =  models.DecimalField(max_digits=6, decimal_places=2)
    max3 =  models.DecimalField(max_digits=6, decimal_places=2)
    max4 =  models.DecimalField(max_digits=6, decimal_places=2)
    max5 =  models.DecimalField(max_digits=6, decimal_places=2)
    max6 =  models.DecimalField(max_digits=6, decimal_places=2)
    max7 =  models.DecimalField(max_digits=6, decimal_places=2)
    max8 =  models.DecimalField(max_digits=6, decimal_places=2)
    max9 =  models.DecimalField(max_digits=6, decimal_places=2)
    max10 = models.DecimalField(max_digits=6, decimal_places=2)
    max11 = models.DecimalField(max_digits=6, decimal_places=2)
    max12 = models.DecimalField(max_digits=6, decimal_places=2)
    max13 = models.DecimalField(max_digits=6, decimal_places=2)
    max14 = models.DecimalField(max_digits=6, decimal_places=2)
    max15 = models.DecimalField(max_digits=6, decimal_places=2)
    max16 = models.DecimalField(max_digits=6, decimal_places=2)
    max17 = models.DecimalField(max_digits=6, decimal_places=2)
    max18 = models.DecimalField(max_digits=6, decimal_places=2)
    max19 = models.DecimalField(max_digits=6, decimal_places=2)
    max20 = models.DecimalField(max_digits=6, decimal_places=2)
    max21 = models.DecimalField(max_digits=6, decimal_places=2)
    max22 = models.DecimalField(max_digits=6, decimal_places=2)
    max23 = models.DecimalField(max_digits=6, decimal_places=2)
    max24 = models.DecimalField(max_digits=6, decimal_places=2)
    max25 = models.DecimalField(max_digits=6, decimal_places=2)
    max26 = models.DecimalField(max_digits=6, decimal_places=2)
    max27 = models.DecimalField(max_digits=6, decimal_places=2)
    max28 = models.DecimalField(max_digits=6, decimal_places=2)
    max29 = models.DecimalField(max_digits=6, decimal_places=2)
    max30 = models.DecimalField(max_digits=6, decimal_places=2)
    max31 = models.DecimalField(max_digits=6, decimal_places=2)
    max32 = models.DecimalField(max_digits=6, decimal_places=2)
    max33 = models.DecimalField(max_digits=6, decimal_places=2)
    max34 = models.DecimalField(max_digits=6, decimal_places=2)
    max35 = models.DecimalField(max_digits=6, decimal_places=2)
    max36 = models.DecimalField(max_digits=6, decimal_places=2)
    max37 = models.DecimalField(max_digits=6, decimal_places=2)
    max38 = models.DecimalField(max_digits=6, decimal_places=2)
    max39 = models.DecimalField(max_digits=6, decimal_places=2)
    max40 = models.DecimalField(max_digits=6, decimal_places=2)
    max41 = models.DecimalField(max_digits=6, decimal_places=2)
    max42 = models.DecimalField(max_digits=6, decimal_places=2)
    max43 = models.DecimalField(max_digits=6, decimal_places=2)
    max44 = models.DecimalField(max_digits=6, decimal_places=2)
    max45 = models.DecimalField(max_digits=6, decimal_places=2)
    max46 = models.DecimalField(max_digits=6, decimal_places=2)
    max47 = models.DecimalField(max_digits=6, decimal_places=2)
    max48 = models.DecimalField(max_digits=6, decimal_places=2)
    max49 = models.DecimalField(max_digits=6, decimal_places=2)
    max50 = models.DecimalField(max_digits=6, decimal_places=2)
    max51 = models.DecimalField(max_digits=6, decimal_places=2)
    max52 = models.DecimalField(max_digits=6, decimal_places=2)
    max53 = models.DecimalField(max_digits=6, decimal_places=2)
    max54 = models.DecimalField(max_digits=6, decimal_places=2)
    max55 = models.DecimalField(max_digits=6, decimal_places=2)
    max56 = models.DecimalField(max_digits=6, decimal_places=2)
    max57 = models.DecimalField(max_digits=6, decimal_places=2)
    max58 = models.DecimalField(max_digits=6, decimal_places=2)
    max59 = models.DecimalField(max_digits=6, decimal_places=2)
    max60 = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.name_list)

class climatic_SensorValue(models.Model):
    name_list = models.CharField(max_length=500)
    value1 =  models.DecimalField(max_digits=6, decimal_places=2)
    value2 =  models.DecimalField(max_digits=6, decimal_places=2)
    value3 =  models.DecimalField(max_digits=6, decimal_places=2)
    value4 =  models.DecimalField(max_digits=6, decimal_places=2)
    value5 =  models.DecimalField(max_digits=6, decimal_places=2)
    value6 =  models.DecimalField(max_digits=6, decimal_places=2)
    value7 =  models.DecimalField(max_digits=6, decimal_places=2)
    value8 =  models.DecimalField(max_digits=6, decimal_places=2)
    value9 =  models.DecimalField(max_digits=6, decimal_places=2)
    value10 = models.DecimalField(max_digits=6, decimal_places=2)
    value11 = models.DecimalField(max_digits=6, decimal_places=2)
    value12 = models.DecimalField(max_digits=6, decimal_places=2)
    value13 = models.DecimalField(max_digits=6, decimal_places=2)
    value14 = models.DecimalField(max_digits=6, decimal_places=2)
    value15 = models.DecimalField(max_digits=6, decimal_places=2)
    value16 = models.DecimalField(max_digits=6, decimal_places=2)
    value17 = models.DecimalField(max_digits=6, decimal_places=2)
    value18 = models.DecimalField(max_digits=6, decimal_places=2)
    value19 = models.DecimalField(max_digits=6, decimal_places=2)
    value20 = models.DecimalField(max_digits=6, decimal_places=2)
    value21 = models.DecimalField(max_digits=6, decimal_places=2)
    value22 = models.DecimalField(max_digits=6, decimal_places=2)
    value23 = models.DecimalField(max_digits=6, decimal_places=2)
    value24 = models.DecimalField(max_digits=6, decimal_places=2)
    value25 = models.DecimalField(max_digits=6, decimal_places=2)
    value26 = models.DecimalField(max_digits=6, decimal_places=2)
    value27 = models.DecimalField(max_digits=6, decimal_places=2)
    value28 = models.DecimalField(max_digits=6, decimal_places=2)
    value29 = models.DecimalField(max_digits=6, decimal_places=2)
    value30 = models.DecimalField(max_digits=6, decimal_places=2)
    value31 = models.DecimalField(max_digits=6, decimal_places=2)
    value32 = models.DecimalField(max_digits=6, decimal_places=2)
    value33 = models.DecimalField(max_digits=6, decimal_places=2)
    value34 = models.DecimalField(max_digits=6, decimal_places=2)
    value35 = models.DecimalField(max_digits=6, decimal_places=2)
    value36 = models.DecimalField(max_digits=6, decimal_places=2)
    value37 = models.DecimalField(max_digits=6, decimal_places=2)
    value38 = models.DecimalField(max_digits=6, decimal_places=2)
    value39 = models.DecimalField(max_digits=6, decimal_places=2)
    value40 = models.DecimalField(max_digits=6, decimal_places=2)
    value41 = models.DecimalField(max_digits=6, decimal_places=2)
    value42 = models.DecimalField(max_digits=6, decimal_places=2)
    value43 = models.DecimalField(max_digits=6, decimal_places=2)
    value44 = models.DecimalField(max_digits=6, decimal_places=2)
    value45 = models.DecimalField(max_digits=6, decimal_places=2)
    value46 = models.DecimalField(max_digits=6, decimal_places=2)
    value47 = models.DecimalField(max_digits=6, decimal_places=2)
    value48 = models.DecimalField(max_digits=6, decimal_places=2)
    value49 = models.DecimalField(max_digits=6, decimal_places=2)
    value50 = models.DecimalField(max_digits=6, decimal_places=2)
    value51 = models.DecimalField(max_digits=6, decimal_places=2)
    value52 = models.DecimalField(max_digits=6, decimal_places=2)
    value53 = models.DecimalField(max_digits=6, decimal_places=2)
    value54 = models.DecimalField(max_digits=6, decimal_places=2)
    value55 = models.DecimalField(max_digits=6, decimal_places=2)
    value56 = models.DecimalField(max_digits=6, decimal_places=2)
    value57 = models.DecimalField(max_digits=6, decimal_places=2)
    value58 = models.DecimalField(max_digits=6, decimal_places=2)
    value59 = models.DecimalField(max_digits=6, decimal_places=2)
    value60 = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.name_list)

class climatic_SensorName(models.Model):
    name_list = models.CharField(max_length=500)
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    name3 = models.CharField(max_length=100)
    name4 = models.CharField(max_length=100)
    name5 = models.CharField(max_length=100)
    name6 = models.CharField(max_length=100)
    name7 = models.CharField(max_length=100)
    name8 = models.CharField(max_length=100)
    name9 = models.CharField(max_length=100)
    name10 = models.CharField(max_length=100)
    name11 = models.CharField(max_length=100)
    name12 = models.CharField(max_length=100)
    name13 = models.CharField(max_length=100)
    name14 = models.CharField(max_length=100)
    name15 = models.CharField(max_length=100)
    name16 = models.CharField(max_length=100)
    name17 = models.CharField(max_length=100)
    name18 = models.CharField(max_length=100)
    name19 = models.CharField(max_length=100)
    name20 = models.CharField(max_length=100)
    name21 = models.CharField(max_length=100)
    name22 = models.CharField(max_length=100)
    name23 = models.CharField(max_length=100)
    name24 = models.CharField(max_length=100)
    name25 = models.CharField(max_length=100)
    name26 = models.CharField(max_length=100)
    name27 = models.CharField(max_length=100)
    name28 = models.CharField(max_length=100)
    name29 = models.CharField(max_length=100)
    name30 = models.CharField(max_length=100)
    name31 = models.CharField(max_length=100)
    name32 = models.CharField(max_length=100)
    name33 = models.CharField(max_length=100)
    name34 = models.CharField(max_length=100)
    name35 = models.CharField(max_length=100)
    name36 = models.CharField(max_length=100)
    name37 = models.CharField(max_length=100)
    name38 = models.CharField(max_length=100)
    name39 = models.CharField(max_length=100)
    name40 = models.CharField(max_length=100)
    name41 = models.CharField(max_length=100)
    name42 = models.CharField(max_length=100)
    name43 = models.CharField(max_length=100)
    name44 = models.CharField(max_length=100)
    name45 = models.CharField(max_length=100)
    name46 = models.CharField(max_length=100)
    name47 = models.CharField(max_length=100)
    name48 = models.CharField(max_length=100)
    name49 = models.CharField(max_length=100)
    name50 = models.CharField(max_length=100)
    name51 = models.CharField(max_length=100)
    name52 = models.CharField(max_length=100)
    name53 = models.CharField(max_length=100)
    name54 = models.CharField(max_length=100)
    name55 = models.CharField(max_length=100)
    name56 = models.CharField(max_length=100)
    name57 = models.CharField(max_length=100)
    name58 = models.CharField(max_length=100)
    name59 = models.CharField(max_length=100)
    name60 = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name_list)

class climatic_MeasureValues(models.Model):
    sensorName_id_fk = models.ForeignKey(climatic_SensorName)
    sensorValue_id_fk = models.ForeignKey(climatic_SensorValue)
    sensorMax_id_fk = models.ForeignKey(climatic_SensorMax)

class climatic_TestLoad(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)

class climatic_AmbientTemp(models.Model):
    value = models.PositiveIntegerField()

    def __str__(self):
        return str(self.value)

class measurement_climatic(measurement):
    """ Climatic measurement specification """
    AmbientTemp = models.ForeignKey(climatic_AmbientTemp)

    TestLoad = models.ForeignKey(climatic_TestLoad)

    sensorTypeList = models.ForeignKey(climatic_SensorTypeList)
    measureValues = models.ForeignKey(climatic_MeasureValues, related_name='soistdasmitdenrelatednames')


    def save(self, *args, **kwargs):
        # set the measurement Type Text
        self.measurement_type = "Climatic"
        # Call the Super Methode
        super(climaticmeasurement, self).save(*args, **kwargs)
