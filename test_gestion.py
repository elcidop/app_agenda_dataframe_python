import unittest

from agenda import gestion

class GestionTest(unittest.TestCase):
    
    
    def test_listar_vacio(self): 
        agenda= gestion.Agenda()       
        lista_contactos=agenda.listar()
        self.assertEqual(len(lista_contactos),0)

    def test_crear(self):       
        agenda= gestion.Agenda()
        agenda.crear('pepe','dsjkfsdl','211546')       
        self.assertEqual( agenda._Agenda__contactos[1].nombre,'PEPE')    
        
    def test_listar_uno(self):
        agenda= gestion.Agenda()
        agenda.crear('pepe','dsjkfsdl','211546')  
        lista_contactos=agenda.listar()
        self.assertEqual(len(lista_contactos),1)
        
    def test_editar_ok(self):
        agenda= gestion.Agenda()
        agenda.crear('pepe','dsjkfsdl','211546') 
        agenda.editar(1,'juan','dsjkfsdl','211546')
        self.assertEqual( agenda._Agenda__contactos[1].nombre,'JUAN') 
    def test_editar_ko(self):
        agenda= gestion.Agenda()
        with self.assertRaises(TypeError):
            agenda.editar(1,'dsjkfsdl','211546')
        
    
    def test_editar_argumentos_ko(self):
        agenda= gestion.Agenda()
        agenda.crear('pepe','dsjkfsdl','211546') 
        with self.assertRaises(Exception):
            agenda.editar(1)  
        with self.assertRaises(Exception):
            agenda.editar(1,'dsjkfsdl')  
        with self.assertRaises(Exception):
            agenda.editar(1,'dsjkfsdl','211546')
        with self.assertRaises(Exception):
            agenda.editar(1,None,'dsjkfsdl','211546')
        with self.assertRaises(Exception):
            agenda.editar(1,'dsjkfsdl',None,'211546')
        agenda.editar(1,'dsjkfsdl','211546',None)
        self.assertIsNone(agenda._Agenda__contactos[1].telefono)
   

if __name__=='__main__':
    unittest.main()