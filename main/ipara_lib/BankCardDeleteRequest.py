# coding=utf-8
import json

from main.posfix_lib.Helper import Helper, HttpClient
from main.posfix_lib.configs import Configs


class BankCardDeleteRequest:
    # Cüzdanda kayıtlı olan kartı silmek için gerekli olan servis girdi
    # parametrelerini temsil eder.
    userId = ""
    cardId = ""
    clientIp = ""

    # Mağazanın, kullanıcının bir kartını veya kayıtlı olan tüm kartlarını
    # silmek istediği zaman kullanabileceği servisi temsil eder.
    def execute(self, req, configs):
        helper = Helper()
        configs.TransactionDate = helper.GetTransactionDateString()

        configs.HashString = configs.PrivateKey+req.userId+req.cardId+req.clientIp +\
            configs.TransactionDate

        json_data = json.dumps(req.__dict__)  # Json Serilestirme

        return HttpClient.post(configs.BaseUrl+"/bankcard/delete",
                               helper.GetHttpHeaders(configs, helper.Application_json), json_data)
