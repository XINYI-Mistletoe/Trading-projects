import requests
import yaml
with open ('env.yaml','r') as f:
    ENV = yaml.safe_load(f)

def main():
    with requests.Session() as s:
        s.headers.update(ENV['API_KEY'])
        mkt_buy_params = {'ticker': 'RGLD', 'type': 'MARKET', 'quantity': 10,'action': 'BUY'}
        resp = s.post('http://localhost:9999/v1/orders', params=mkt_buy_params)
        print(resp)
        if resp.ok:
            mkt_order = resp.json()
            id = mkt_order['order_id']
            print('The market buy order was submitted and has ID', id)
        else:
            print('The order was not successfully submitted!')
if __name__ == '__main__':
    main()