from discordwebhook import Discord

discord = Discord(url="https://discord.com/api/webhooks/1323483640390488134/wllh4ktEsqx_hShQQ7n-kAmFm4Pbs0JnMDQyLk73cx0sR690K2QPNhu0wzk-9ytP6yhj")
discord.post(
    embeds=[
        {
            "title": "ตรวจพบเปลวไฟ",
            "fields": [
                {"name": "ระดับเปลวไฟ", "value": "level", "inline": True},
                {"name": "ผู้คนในพื้นที่", "value": "คน", "inline": True}
            ]
        }
    ],
)