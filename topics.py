def compare_subs(topic, mqtt_topic_prefix, target_device):
    if topic == '{device_id}/shadow/get/accepted':
        topic = target_device +'/shadow/get/accepted'
    elif topic == '$aws/things/{device_id}/shadow/get/rejected':
        topic = '$aws/things/' + target_device + '/shadow/get/rejected'
    elif topic == '$aws/things/{device_id}/shadow/update/delta':
        topic = '$aws/things/', target_device + '/shadow/update/delta'
    elif topic == 'mqtt_topic_prefix/m/d/{device_id}/d2c':
        topic = mqtt_topic_prefix + 'm/d/' + target_device + '/d2c'
    elif topic == 'mqtt_topic_prefix/m/d/{device_id}/c2d':
        topic = mqtt_topic_prefix + 'm/d/'+ target_device + '/c2d'
    elif topic == 'matt_topic_prefix/{device_id}/jobs/rcv':
        topic = mqtt_topic_prefix + target_device + '/jobs/rcv'
    elif topic == 'm/#':
        topic = mqtt_topic_prefix + 'm/#'
    elif topic == 'a/connections':
        topic = mqtt_topic_prefix + 'a/connections'
    else:
        topic = topic  #user manual input
    print(topic)
    return topic

def compare_pubs(topic, mqtt_topic_prefix, target_device):
    if topic == '$aws/things/{device_id}/shadow/get':
        topic = '$aws/things/' + target_device + '/shadow/get'
    elif topic == '$aws/things/{device_id}/shadow/update':
        topic = '$aws/things/' + target_device + '/shadow/update'
    elif topic == 'mqtt_topic_prefix/m/d/{device_id}/d2c':
        topic = mqtt_topic_prefix + 'm/d/' + target_device + '/d2c'
    elif topic == 'mqtt_topic_prefix/m/d/{device_id}/d2c/bulk':
        topic = mqtt_topic_prefix + 'm/d/' + target_device + '/d2c/bulk'
    elif topic == 'mqtt_topic_prefix/{device_id}/jobs/req':
        topic = mqtt_topic_prefix + target_device + '/jobs/req'
    elif topic == 'mqtt_topic_prefix/{device_id}/jobs/update':
        topic = mqtt_topic_prefix + target_device + '/jobs/update'
    elif topic == 'mqtt_topic_prefix/m/#':
        topic = mqtt_topic_prefix + 'm/#'
    else:
        topic = topic #user custom input
    print(topic)
    return topic

def shorten_topic(topic):
    if topic == '{device_id}/shadow/get/accepted':
        topic = '/shadow/get/accepted'
    elif topic == '$aws/things/{device_id}/shadow/get/rejected':
        topic = '/shadow/get/rejected'
    elif topic == '$aws/things/{device_id}/shadow/update/delta':
        topic = '/shadow/update/delta'
    elif topic == 'mqtt_topic_prefix/m/d/{device_id}/d2c':
        topic = '/d2c'
    elif topic == 'mqtt_topic_prefix/m/d/{device_id}/c2d':
        topic = 'c2d'
    elif topic == 'matt_topic_prefix/{device_id}/jobs/rcv':
        topic = 'jobs/rcv'
    elif topic == 'm/#':
        topic = 'm/#'
    elif topic == 'a/connections':
        topic = 'a/connections'
    else:
        topic = topic  #user manual input
    print(topic)
    return topic