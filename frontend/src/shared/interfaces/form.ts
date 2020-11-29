export interface FieldData {
  name: string[];
  value: any;
  touched: boolean;
  validating: boolean;
  errors: string[];
}

export interface FormData {
  fields: FieldData[];
  onChange: (fields: FieldData[]) => void;
}