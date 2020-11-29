import React, {FC} from 'react';
import {useHistory, useLocation} from 'react-router-dom';
import {Button, Layout} from 'antd';
import Header from '../Header';
import './PageLayout.scss';
import {ArrowLeftOutlined} from '@ant-design/icons';


const PageLayout: FC<any> = ({children}) => {
  const location = useLocation();
  const history = useHistory();

  return (
    <>
      <Layout className="layout">
        <Header />
        <Layout>
          <Layout.Content className="layout-content" style={{padding: '0 50px', marginTop: 64}}>
            <div className="site-layout-content">
              { location.pathname !== '/' &&
                <Button type="primary" onClick={() => history.goBack()} style={{marginBottom: 16, marginLeft: 16, float: 'right'}}>
                  <ArrowLeftOutlined />
                  Назад
                </Button>
              }
              {children}
            </div>
          </Layout.Content>
        </Layout>
        <Layout.Footer style={{textAlign: 'center'}}>
          Сердце ©2020 Created by NOVA
        </Layout.Footer>
      </Layout>
    </>
  );
};

export default PageLayout;
  