import React, {FC} from 'react';
import {Form, Input, Button, Radio, Upload, Select, InputNumber, Modal, Image} from 'antd';
import {UploadOutlined} from '@ant-design/icons';
import {ClientFormData} from '../../interfaces/client';
import {request} from '../../utils/api';

const {Option} = Select;

const ClientForm: FC<ClientFormData> = ({client}) => {

  const formItemLayout = {
    labelCol: {span: 6},
    wrapperCol: {span: 14},
  };

  const showModal = (content: string, type?: string) => {
    switch (type) {
      case 'error':
        Modal.error({title: 'Ошибка', content: (<div>{content}</div>), onOk() {}});
        break;
      case 'warning':
        Modal.warning({title: 'Внимание', content: (<div>{content}</div>), onOk() {}});
        break;
      case 'success':
        Modal.success({title: 'Отлично', content: (<div>{content}</div>), onOk() {}});
        break;
      default:
        Modal.info({title: 'Внимание', content: (<div>{content}</div>), onOk() {}});
        break;
    }
  }

  const onFinish = (values: any) => {
    const url = client?.id ? `client/${client.id}/edit` : 'client/add';

    request(url, {
      method: 'POST',
      body: JSON.stringify(values)
    })
      .then(r => r.json())
      .then(r => {
        if (r?.status === 'success') {
          showModal(r?.message, 'success');
        } else {
          showModal('Возникла ошибка на сервере, повторите попытку позднее', 'error');
        }
      });
  };

  const onFinishFailed = (errorInfo: any) => {
    showModal(errorInfo, 'error');
  };

  const normFile = (e: { fileList: any; }) => {
    console.log('Upload event:', e);
    if (Array.isArray(e)) {
      return e;
    }
    return e && e.fileList;
  };

  return (
    <div style={{clear: 'both'}}>
            <Form
              name="basic"
              {...formItemLayout}
              initialValues={{...client}}
              onFinish={onFinish}
              onFinishFailed={onFinishFailed}
            >

                <Form.Item
                  label="Образование"
                  name="study"
                >
                    <Input />
                </Form.Item>

                <Form.Item
                  label="Национальность"
                  name="national"
                >
                    <Input />
                </Form.Item>

                <Form.Item
                  label="Профессия"
                  name="profession"
                >
                    <Input />
                </Form.Item>

                <Form.Item
                  label="Религия"
                  name="religion"
                >
                    <Input />
                </Form.Item>

                <Form.Item
                  label="Семейное положение"
                  name="family"
                >
                    <Input />
                </Form.Item>

                <Form.Item
                  label="Возраст"
                  name="age"
                  rules={[{required: true}]}
                >
                   <InputNumber min={1} max={100} />
                </Form.Item>

                <Form.Item name="sex" label="Пол">
                    <Radio.Group>
                        <Radio value="М">Мужской</Radio>
                        <Radio value="Ж">Женский</Radio>
                    </Radio.Group>
                </Form.Item>

                <Form.Item name="working" label="Работает">
                    <Radio.Group>
                        <Radio value="1">Да</Radio>
                        <Radio value="0">Нет</Radio>
                    </Radio.Group>
                </Form.Item>

                <Form.Item name="pension" label="На пенсии">
                    <Radio.Group>
                        <Radio value="1">Да</Radio>
                        <Radio value="0">Нет</Radio>
                    </Radio.Group>
                </Form.Item>

                <Form.Item name="work_end_by_ill" label="Прекращение работы по болезни">
                    <Radio.Group>
                        <Radio value="1">Да</Radio>
                        <Radio value="0">Нет</Radio>
                    </Radio.Group>
                </Form.Item>

                <Form.Item name="diabet" label="Диабет">
                    <Radio.Group>
                        <Radio value="1">Да</Radio>
                        <Radio value="0">Нет</Radio>
                    </Radio.Group>
                </Form.Item>

                <Form.Item
                   label="Длительность диабета"
                   name="diabet_long"
                >
                   <InputNumber min={0} max={100} />
                </Form.Item>


                <Form.Item
                  name="areaType"
                  label="Тип населённого пункта"
                  hasFeedback
                  rules={[{required: true, message: 'Выберите тип населённого пункта'}]}
                >
                    <Select placeholder="Выберите тип населённого пункта">
                        <Option value="1">Город</Option>
                        <Option value="2">Село</Option>
                    </Select>
                </Form.Item>

                <Form.Item
                  name="cardioFile"
                  label="Кардиограмма"
                  valuePropName="cardioFile"
                  getValueFromEvent={normFile}
                >
                    <Upload listType="picture">
                        <Button icon={<UploadOutlined />}>Загрузить</Button>
                    </Upload>
                </Form.Item>

                <Form.Item>
                    <Button type="primary" htmlType="submit">
                        Сохранить
                    </Button>
                </Form.Item>
            </Form>
        </div>

  );
};

export default ClientForm;
