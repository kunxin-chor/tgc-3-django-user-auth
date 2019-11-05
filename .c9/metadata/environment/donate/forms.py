{"changed":true,"filter":false,"title":"forms.py","tooltip":"/donate/forms.py","value":"","undoManager":{"mark":11,"position":70,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":9},"action":"insert","lines":["from .models import Charge","","class OrderForm(forms.ModelForm):","","    class Meta:","        model = Charge","        fields = (","            'full_name', 'phone_number', 'country', 'postcode',","            'town_or_city', 'street_address1', 'street_address2',","            'county'","        )"],"id":1}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":2},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["`"],"id":3}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["`"],"id":4}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "],"id":5}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"],"id":6},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":[" "],"id":7},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["d"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["j"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["a"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["n"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["g"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["o"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["."]}],[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"remove","lines":["."],"id":8}],[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":[" "],"id":9},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["i"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["m"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["p"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["o"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["r"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["t"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":[" "],"id":10},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["f"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["o"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["r"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["m"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":25},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"remove","lines":["s"],"id":12}],[{"start":{"row":10,"column":9},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]},{"start":{"row":11,"column":8},"end":{"row":12,"column":0},"action":"insert","lines":["",""]},{"start":{"row":12,"column":0},"end":{"row":12,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "],"id":14},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["c"],"id":15},{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":["l"]},{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"insert","lines":["a"]},{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"insert","lines":["s"]},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["s"],"id":16}],[{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"remove","lines":["s"],"id":17},{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"remove","lines":["a"]},{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"remove","lines":["l"]},{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":["c"]}],[{"start":{"row":12,"column":0},"end":{"row":21,"column":57},"action":"insert","lines":["class PaymentForm(forms.Form):","","    MONTH_CHOICES = [(i, i) for i in range(1, 12)]","    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]","","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)"],"id":18}],[{"start":{"row":14,"column":50},"end":{"row":14,"column":51},"action":"insert","lines":[" "],"id":19},{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"insert","lines":["$"]}],[{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"remove","lines":["$"],"id":20}],[{"start":{"row":14,"column":51},"end":{"row":14,"column":52},"action":"insert","lines":["#"],"id":21}],[{"start":{"row":14,"column":52},"end":{"row":14,"column":53},"action":"insert","lines":[" "],"id":22}],[{"start":{"row":14,"column":53},"end":{"row":14,"column":55},"action":"insert","lines":["[]"],"id":23}],[{"start":{"row":14,"column":54},"end":{"row":14,"column":55},"action":"insert","lines":[" "],"id":24}],[{"start":{"row":14,"column":55},"end":{"row":14,"column":57},"action":"insert","lines":["()"],"id":25}],[{"start":{"row":14,"column":56},"end":{"row":14,"column":57},"action":"insert","lines":["1"],"id":26},{"start":{"row":14,"column":57},"end":{"row":14,"column":58},"action":"insert","lines":[","]},{"start":{"row":14,"column":58},"end":{"row":14,"column":59},"action":"insert","lines":["1"]}],[{"start":{"row":14,"column":60},"end":{"row":14,"column":61},"action":"insert","lines":[","],"id":27}],[{"start":{"row":14,"column":61},"end":{"row":14,"column":62},"action":"insert","lines":[" "],"id":28}],[{"start":{"row":14,"column":62},"end":{"row":14,"column":64},"action":"insert","lines":["()"],"id":29}],[{"start":{"row":14,"column":63},"end":{"row":14,"column":64},"action":"insert","lines":["2"],"id":30},{"start":{"row":14,"column":64},"end":{"row":14,"column":65},"action":"insert","lines":[","]},{"start":{"row":14,"column":65},"end":{"row":14,"column":66},"action":"insert","lines":["2"]}],[{"start":{"row":14,"column":67},"end":{"row":14,"column":68},"action":"insert","lines":[","],"id":31}],[{"start":{"row":14,"column":68},"end":{"row":14,"column":69},"action":"insert","lines":[" "],"id":32}],[{"start":{"row":14,"column":69},"end":{"row":14,"column":71},"action":"insert","lines":["()"],"id":33}],[{"start":{"row":14,"column":70},"end":{"row":14,"column":71},"action":"insert","lines":["3"],"id":34},{"start":{"row":14,"column":71},"end":{"row":14,"column":72},"action":"insert","lines":["m"]},{"start":{"row":14,"column":72},"end":{"row":14,"column":73},"action":"insert","lines":["3"]}],[{"start":{"row":14,"column":72},"end":{"row":14,"column":73},"action":"remove","lines":["3"],"id":35},{"start":{"row":14,"column":71},"end":{"row":14,"column":72},"action":"remove","lines":["m"]}],[{"start":{"row":14,"column":71},"end":{"row":14,"column":72},"action":"insert","lines":[","],"id":36},{"start":{"row":14,"column":72},"end":{"row":14,"column":73},"action":"insert","lines":["3"]}],[{"start":{"row":14,"column":74},"end":{"row":14,"column":75},"action":"insert","lines":[","],"id":37}],[{"start":{"row":14,"column":75},"end":{"row":14,"column":76},"action":"insert","lines":[" "],"id":38},{"start":{"row":14,"column":76},"end":{"row":14,"column":77},"action":"insert","lines":["9"]}],[{"start":{"row":14,"column":76},"end":{"row":14,"column":77},"action":"remove","lines":["9"],"id":39}],[{"start":{"row":14,"column":76},"end":{"row":14,"column":78},"action":"insert","lines":["()"],"id":40}],[{"start":{"row":14,"column":77},"end":{"row":14,"column":78},"action":"insert","lines":["4"],"id":41},{"start":{"row":14,"column":78},"end":{"row":14,"column":79},"action":"insert","lines":[","]},{"start":{"row":14,"column":79},"end":{"row":14,"column":80},"action":"insert","lines":["4"]}],[{"start":{"row":14,"column":81},"end":{"row":14,"column":82},"action":"insert","lines":[" "],"id":42},{"start":{"row":14,"column":82},"end":{"row":14,"column":83},"action":"insert","lines":["."]},{"start":{"row":14,"column":83},"end":{"row":14,"column":84},"action":"insert","lines":["."]},{"start":{"row":14,"column":84},"end":{"row":14,"column":85},"action":"insert","lines":["."]}],[{"start":{"row":14,"column":85},"end":{"row":14,"column":86},"action":"insert","lines":[" "],"id":43}],[{"start":{"row":15,"column":54},"end":{"row":15,"column":55},"action":"insert","lines":[" "],"id":44},{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"insert","lines":["#"]}],[{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":[" "],"id":45}],[{"start":{"row":15,"column":57},"end":{"row":15,"column":59},"action":"insert","lines":["[]"],"id":46}],[{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":[" "],"id":47}],[{"start":{"row":15,"column":59},"end":{"row":15,"column":61},"action":"insert","lines":["()"],"id":48}],[{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"insert","lines":["2"],"id":49},{"start":{"row":15,"column":61},"end":{"row":15,"column":62},"action":"insert","lines":["0"]},{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"insert","lines":["1"]},{"start":{"row":15,"column":63},"end":{"row":15,"column":64},"action":"insert","lines":["9"]},{"start":{"row":15,"column":64},"end":{"row":15,"column":65},"action":"insert","lines":[","]}],[{"start":{"row":15,"column":65},"end":{"row":15,"column":66},"action":"insert","lines":[" "],"id":50},{"start":{"row":15,"column":66},"end":{"row":15,"column":67},"action":"insert","lines":["2"]},{"start":{"row":15,"column":67},"end":{"row":15,"column":68},"action":"insert","lines":["0"]},{"start":{"row":15,"column":68},"end":{"row":15,"column":69},"action":"insert","lines":["1"]},{"start":{"row":15,"column":69},"end":{"row":15,"column":70},"action":"insert","lines":["9"]}],[{"start":{"row":15,"column":71},"end":{"row":15,"column":72},"action":"insert","lines":[","],"id":51}],[{"start":{"row":15,"column":72},"end":{"row":15,"column":73},"action":"insert","lines":[" "],"id":52}],[{"start":{"row":15,"column":73},"end":{"row":15,"column":75},"action":"insert","lines":["()"],"id":53}],[{"start":{"row":15,"column":74},"end":{"row":15,"column":75},"action":"insert","lines":["2"],"id":54},{"start":{"row":15,"column":75},"end":{"row":15,"column":76},"action":"insert","lines":["0"]},{"start":{"row":15,"column":76},"end":{"row":15,"column":77},"action":"insert","lines":["2"]},{"start":{"row":15,"column":77},"end":{"row":15,"column":78},"action":"insert","lines":["0"]},{"start":{"row":15,"column":78},"end":{"row":15,"column":79},"action":"insert","lines":[","]}],[{"start":{"row":15,"column":79},"end":{"row":15,"column":80},"action":"insert","lines":[" "],"id":55},{"start":{"row":15,"column":80},"end":{"row":15,"column":81},"action":"insert","lines":["2"]},{"start":{"row":15,"column":81},"end":{"row":15,"column":82},"action":"insert","lines":["0"]},{"start":{"row":15,"column":82},"end":{"row":15,"column":83},"action":"insert","lines":["2"]},{"start":{"row":15,"column":83},"end":{"row":15,"column":84},"action":"insert","lines":["0"]}],[{"start":{"row":15,"column":85},"end":{"row":15,"column":86},"action":"insert","lines":[","],"id":56}],[{"start":{"row":15,"column":86},"end":{"row":15,"column":87},"action":"insert","lines":[" "],"id":57}],[{"start":{"row":15,"column":87},"end":{"row":15,"column":89},"action":"insert","lines":["()"],"id":58}],[{"start":{"row":15,"column":88},"end":{"row":15,"column":89},"action":"insert","lines":["2"],"id":59},{"start":{"row":15,"column":89},"end":{"row":15,"column":90},"action":"insert","lines":["0"]},{"start":{"row":15,"column":90},"end":{"row":15,"column":91},"action":"insert","lines":["2"]},{"start":{"row":15,"column":91},"end":{"row":15,"column":92},"action":"insert","lines":["1"]},{"start":{"row":15,"column":92},"end":{"row":15,"column":93},"action":"insert","lines":[","]}],[{"start":{"row":15,"column":93},"end":{"row":15,"column":94},"action":"insert","lines":[" "],"id":60},{"start":{"row":15,"column":94},"end":{"row":15,"column":95},"action":"insert","lines":["2"]},{"start":{"row":15,"column":95},"end":{"row":15,"column":96},"action":"insert","lines":["0"]},{"start":{"row":15,"column":96},"end":{"row":15,"column":97},"action":"insert","lines":["2"]},{"start":{"row":15,"column":97},"end":{"row":15,"column":98},"action":"insert","lines":["1"]}],[{"start":{"row":15,"column":99},"end":{"row":15,"column":100},"action":"insert","lines":[" "],"id":61}],[{"start":{"row":15,"column":99},"end":{"row":15,"column":100},"action":"remove","lines":[" "],"id":62}],[{"start":{"row":15,"column":99},"end":{"row":15,"column":100},"action":"insert","lines":["."],"id":63},{"start":{"row":15,"column":100},"end":{"row":15,"column":101},"action":"insert","lines":["."]},{"start":{"row":15,"column":101},"end":{"row":15,"column":102},"action":"insert","lines":["."]}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":64}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":65}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["#"],"id":66}],[{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":[" "],"id":67},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["u"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["s"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":[" "],"id":68},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["l"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["s"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["i"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":[" "],"id":69},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["c"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"remove","lines":["o"],"id":70},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"remove","lines":["c"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":[" "]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["t"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["i"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["s"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["i"],"id":71},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["s"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":102,"scrollleft":0,"selection":{"start":{"row":14,"column":14},"end":{"row":14,"column":14},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1572843166491}