import React, {useEffect, useState} from 'react';
import './styles.scss';
import {Link, useRouteMatch} from 'react-router-dom';
import {Button, Skeleton} from 'antd';
import {UserOutlined} from '@ant-design/icons';
import {RouteParams} from '../../shared/interfaces/route';
import {Client} from '../../shared/interfaces/client';
import {request} from '../../shared/utils/api';
import ClientForm from "../../shared/components/ClientForm";

const ClientEdit = () => {
  const params = useRouteMatch<RouteParams>('/client/:id');
  const [client, setClient] = useState<Client | null>(null);

  useEffect(() => {
    request(`client/${params?.params?.id}`, {
      method: 'GET'
    }).then((r) => {
      setClient(r);
    });
  }, [params?.params?.id]);

  return (
    <div>
      {!client && <Skeleton active />}

      {
        client &&
        <>
          <Link to={`/client/${client.id}`}>
            <Button type="primary" style={{marginBottom: 16, float: 'right'}}>
              <UserOutlined />
              Посмотреть
            </Button>
          </Link>
            Редактирование анкеты
            <ClientForm
              client={client}
            />
        </>
      }
    </div>
  );
};

export default ClientEdit;
