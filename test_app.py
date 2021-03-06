import os   
import tempfile           
    
    
import pytest    
    
         
from server import app                                  
from quiz_card.extensions import db    
                                                
                                                                    
@pytest.fixture                                    
def client():    
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()    
    app.config['TESTING'] = True                
    with app.test_client() as client:           
        with app.app_context():     
            db.init_app(app)    
        yield client    
    os.close(db_fd)    
    os.unlink(app.config['DATABASE']) 

