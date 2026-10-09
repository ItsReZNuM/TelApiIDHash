from bs4 import BeautifulSoup
import main


def test_standard_markup():
    html = '''
    <div class="form-group">
      <label for="app_id" class="col-md-3 control-label">App api_id:</label>
      <div class="col-md-9">
        <span class="form-control input-xlarge uneditable-input" onclick="this.select();"><strong>1234567</strong></span>
      </div>
    </div>
    <div class="form-group">
      <label for="app_hash" class="col-md-3 control-label">App api_hash:</label>
      <div class="col-md-9">
        <span class="form-control input-xlarge uneditable-input" onclick="this.select();">0123456789abcdef0123456789abcdef</span>
      </div>
    </div>
    <div class="form-group">
      <label class="col-md-3 control-label">Public keys:</label>
      <div class="col-md-9"><code>-----BEGIN RSA PUBLIC KEY-----xyz-----END RSA PUBLIC KEY-----</code></div>
    </div>
    <div class="form-group">
      <label class="col-md-3 control-label">Production configuration:</label>
      <div class="col-md-9"><strong>149.154.167.50:443</strong></div>
    </div>
    '''
    soup = BeautifulSoup(html, 'html.parser')
    api_id, api_hash, key, pc = main.extract_credentials(html, soup)
    assert api_id == '1234567'
    assert api_hash == '0123456789abcdef0123456789abcdef'
    assert 'RSA PUBLIC KEY' in key
    assert pc == '149.154.167.50:443'


def test_whitespace_and_custom_markup():
    html = '''
    <div>
      <label>
        App api_id: 
      </label>
      <div>
        <input type="text" value="98765432" />
      </div>
      <label>
        App api_hash:
      </label>
      <div>
        <span>abcdef0123456789abcdef0123456789</span>
      </div>
    </div>
    '''
    soup = BeautifulSoup(html, 'html.parser')
    api_id, api_hash, key, pc = main.extract_credentials(html, soup)
    assert api_id == '98765432'
    assert api_hash == 'abcdef0123456789abcdef0123456789'
    assert key is None
    assert pc is None


def test_regex_fallback():
    # When HTML tags are irregular or stripped
    html = '''
    Some text with App api_id: 55443322 and App api_hash: fedcba9876543210fedcba9876543210
    '''
    soup = BeautifulSoup(html, 'html.parser')
    api_id, api_hash, key, pc = main.extract_credentials(html, soup)
    assert api_id == '55443322'
    assert api_hash == 'fedcba9876543210fedcba9876543210'


if __name__ == '__main__':
    test_standard_markup()
    test_whitespace_and_custom_markup()
    test_regex_fallback()
    print("All tests passed successfully!")
