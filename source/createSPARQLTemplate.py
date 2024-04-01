import myGraphDB as gdb
import myLib


if __name__ == '__main__':

    templateId = 'http://cmdx.u-tokyo.ac.jp/templates/updateIlluminanceSensor'
    filepath = myLib.dataDir + 'sparqlTemplate_updateSensor_ill.txt'
    r = gdb.create_sparql_template_from_file(myLib.baseUrl, myLib.repoId, templateId, filepath)
    print(r.text)


    templateId = 'http://cmdx.u-tokyo.ac.jp/templates/updateShtSensor'
    filepath = myLib.dataDir + 'sparqlTemplate_updateSensor_sht.txt'
    r = gdb.create_sparql_template_from_file(myLib.baseUrl, myLib.repoId, templateId, filepath)
    print(r.text)
   

    templateId = 'http://cmdx.u-tokyo.ac.jp/templates/updateIRSensor'
    filepath = myLib.dataDir + 'sparqlTemplate_updateSensor_ir.txt'
    r = gdb.create_sparql_template_from_file(myLib.baseUrl, myLib.repoId, templateId, filepath)
    print(r.text)
