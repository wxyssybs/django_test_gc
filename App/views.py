from time import sleep

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from App.signals.handlers import my_signal


def home(request):
    # my_signal.send(home, name='gc')
    a = 1/0
    return JsonResponse({
        "message": "请求成功",
        "data": [
            {
                "asset_status": 0,
                "asset_operator_org": 0,
                "ip": "10.132.20.43",
                "hardware": {
                    "disk_capacity": "1 X 430G",
                    "mem": "[{\"type\": \"Unknown\", \"details\": [{\"manufacture\": null, \"maxspeed\": null, \"runspeed\": null, \"sn\": null, \"pn\": null, \"size\": \"16 GB\"}], \"slotarry\": 1, \"slotmax\": 1, \"total\": \"16GB\", \"speed\": null}]",
                    "cpu": "[{\"physicsprocess\": 8, \"HT\": \"disable\", \"threads\": \"1\", \"cores\": \"1\", \"model\": \"QEMU Virtual CPU version (cpu64-rhel6)\", \"speed\": \"2394.454\"}]",
                    "net": "[{\"ip\": \"10.132.20.43\", \"mac\": \"eth0\", \"carrier\": \"1\", \"PhysDevice\": \"\", \"Device\": \"eth0\", \"speed\": null}]",
                    "disk": "[{\"controller\": [\"Xen Disk controller\"], \"disks\": [{\"RPM\": \"\", \"model\": \"XenVirtioDisk\", \"speed\": \"\", \"name\": \"XenVirtioDisk vda\", \"size\": \"430G\"}]}]",
                    "id": 3997348752422
                },
                "assetno": None,
                "tx_sn": "",
                "type": "虚拟机",
                "id": 4545040745875,
                "asset_status_message": "自有",
                "producer": "58vm",
                "hostname": "tjtxvm132-20-43.58os.org",
                "environment": "online",
                "server_ip": "10.132.20.43",
                "status_message": "已交付",
                "status": 200,
                "assettype": 0,
                "masterip": "10.135.2.133",
                "business": [
                    {
                        "qa": "于伯伟(yubowei)",
                        "qam": "于伯伟(yubowei)",
                        "opsowner": "李晖(lihui41),戴靖洋(daijingyang),高晨(gaochen01)",
                        "rd": "高歌(gaoge05),金海兰(jinhailan),郭光福(guoguangfu),刘春雷(liuchunlei04),张广元(zhangguangyuan),于伯伟(yubowei),李晖(lihui41),沙文强(shawenqiang),刘汉生(liuhansheng)",
                        "cluster": "DB_cdb",
                        "bizowner": "高歌(gaoge05),金海兰(jinhailan),郭光福(guoguangfu),刘春雷(liuchunlei04),张广元(zhangguangyuan),于伯伟(yubowei),李晖(lihui41),沙文强(shawenqiang),刘汉生(liuhansheng)",
                        "rdm": "于伯伟(yubowei)",
                        "opm": "刘春雷(liuchunlei04),于伯伟(yubowei)",
                        "busline": "TEG",
                        "op": "李晖(lihui41),戴靖洋(daijingyang),高晨(gaochen01)"
                    },
                    {
                        "qa": "刘春雷(liuchunlei04),戴靖洋(daijingyang),李晖(lihui41),金海兰(jinhailan)",
                        "qam": "于伯伟(yubowei)",
                        "opsowner": "李晖(lihui41),戴靖洋(daijingyang),高晨(gaochen01)",
                        "rd": "刘春雷(liuchunlei04),高晨(gaochen01),戴靖洋(daijingyang),金海兰(jinhailan),李晖(lihui41)",
                        "cluster": "DB_cdb_backend_online",
                        "bizowner": "刘春雷(liuchunlei04),高晨(gaochen01),戴靖洋(daijingyang),金海兰(jinhailan),李晖(lihui41)",
                        "rdm": "于伯伟(yubowei)",
                        "opm": "刘春雷(liuchunlei04),于伯伟(yubowei)",
                        "busline": "TEG",
                        "op": "李晖(lihui41),戴靖洋(daijingyang),高晨(gaochen01)"
                    },
                    {
                        "qa": "李晖(lihui41)",
                        "qam": "于伯伟(yubowei)",
                        "opsowner": "李晖(lihui41),戴靖洋(daijingyang),高晨(gaochen01)",
                        "rd": "李晖(lihui41)",
                        "cluster": "DB_cdb_h5_online",
                        "bizowner": "李晖(lihui41)",
                        "rdm": "于伯伟(yubowei)",
                        "opm": "刘春雷(liuchunlei04),于伯伟(yubowei)",
                        "busline": "TEG",
                        "op": "李晖(lihui41),戴靖洋(daijingyang),高晨(gaochen01)"
                    },
                    {
                        "qa": "高晨(gaochen01),戴靖洋(daijingyang),李晖(lihui41)",
                        "qam": "于伯伟(yubowei)",
                        "opsowner": "李晖(lihui41),戴靖洋(daijingyang),高晨(gaochen01)",
                        "rd": "高晨(gaochen01),戴靖洋(daijingyang),李晖(lihui41)",
                        "cluster": "DB_cdb_web_online",
                        "bizowner": "高晨(gaochen01),戴靖洋(daijingyang),李晖(lihui41)",
                        "rdm": "于伯伟(yubowei)",
                        "opm": "刘春雷(liuchunlei04),于伯伟(yubowei)",
                        "busline": "TEG",
                        "op": "李晖(lihui41),戴靖洋(daijingyang),高晨(gaochen01)"
                    }
                ],
                "allocation": 1,
                "inc_model": "VC1",
                "producermodel": "VM",
                "runstatuscode": 0,
                "onshelftime": "",
                "sn_no": "vm_10.132.20.43",
                "runstatus": "正常",
                "idc": "tjtx",
                "agentversion": "247",
                "position": "tjtx-M203-D07-4",
                "use_state": 1,
                "os": {
                    "kernerl": "",
                    "version": "centos6.6",
                    "type": "Linux"
                },
                "asset_operator_org_message": "58",
                "warrantyduetime": "",
                "type_code": 2
            }
        ],
        "statuscode": 0
    }
    )
