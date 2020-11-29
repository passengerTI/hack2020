import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom';
import {Table, Row, Col, Button, Card, Statistic} from 'antd';
import './styles.scss';
import {request} from '../../shared/utils/api';
import {FormOutlined, UserOutlined, UserAddOutlined, ArrowUpOutlined, ArrowDownOutlined} from '@ant-design/icons';

const Clients = () => {
  const [clients, setClients] = useState([]);
  const [tableLoading, setTableLoading] = useState(true);

  const columns = [
    {
      title: 'ID',
      dataIndex: 'id'
    },
    {
      title: 'Место проживания',
      dataIndex: 'areaType',
      render: (areaType: number) => areaType === 1 ? 'Город' : 'Село'
    },
    {
      title: 'Дата рождения',
      dataIndex: 'birthday'
    },
    {
      title: 'Возраст',
      dataIndex: 'age'
    },
    {
      title: 'Действия',
      dataIndex: 'id',
      render: (id: string) => (
        <>
          <Link to={`/client/${id}`}>
            <Button type="primary">
              <UserOutlined />
              Открыть
            </Button>
          </Link>
          &nbsp;&nbsp;
          <Link to={`/client/${id}/edit`}>
            <Button type="primary">
              <FormOutlined />
              Изменить
            </Button>
          </Link>
        </>
      )
    },
  ];

  useEffect(() => {
    request('clients', {
      method: 'GET'
    }).then((r) => {
      setClients(r);
      setTableLoading(false);
    });
  }, []);

  return (
    <div>
       <Row gutter={16} style={{marginBottom: 16}}>
        <Col span={6}>
          <Card>
            <Statistic
              title="Рост группы риска по ССЗ"
              value={4.28}
              precision={2}
              valueStyle={{color: '#cf1322'}}
              prefix={<ArrowUpOutlined />}
              suffix="%"
            />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic
              title="Процент острых проявлений"
              value={2.3}
              precision={2}
              valueStyle={{color: '#3f8600'}}
              prefix={<ArrowDownOutlined />}
              suffix="%"
            />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic
              title="Прирост диспансеризации или обследований по ССЗ"
              value={592}
              valueStyle={{color: '#3f8600'}}
              prefix={<ArrowUpOutlined />}
              suffix="за день"
            />
          </Card>
        </Col>
        <Col span={6}>
          <Card>
            <Statistic
              title="Количество обработанных диспансеризаций"
              value={1279}
              valueStyle={{color: '#3f8600'}}
              prefix={<ArrowUpOutlined />}
              suffix="за день"
            />
          </Card>
        </Col>
      </Row>
      <Row>
        <Col span={24}>
          <Link to="/client/add">
            <Button type="primary" style={{marginBottom: 16, float: 'right'}}>
              <UserAddOutlined />
              Добавить анкету
            </Button>
          </Link>
          <Table
            rowKey="id"
            columns={columns}
            dataSource={clients}
            loading={tableLoading}
            title={() => 'Анкеты'}
            bordered
          />
        </Col>
      </Row>
    </div>
  );
};

export default Clients;
  